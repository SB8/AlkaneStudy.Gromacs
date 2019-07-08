
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '1024xC15-AA_3nsEq.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '72', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.L_OPLS
mdpFF['tau-p'] = '4.0' # Add mdpFF after ensemble in mdp list to overwrite e.g. [mdp.NPT_eq, mdpFF]

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# Energy minimization
newSim = SimGromacs([mdpFF, mdp.EM], shellFile, 
			mdrun=mdrunCmd,
			suffix='EM', 
			traj='trr',
			coords=currentCoords)
# This stores the filename of the current coordinate file (.gro)
coordsEM = newSim.coordsOut
# Write EM to file
finalize_simulation(newSim, shellFile, outputDir)

n_runs = 5

for i in range(0, n_runs, 1):

	# Equilibration at atmospheric pressure (using gen-vel = yes)
	newSim = SimGromacs([mdp.NPT_eq, mdpFF], shellFile, 
				mdrun=mdrunCmd,
				mdpSuffix='NPT_eq',
				suffix='NPT_eq_'+str(i),
				coords=coordsEM)
	currentCoords = newSim.coordsOut
	newSim.set_param('nsteps', 2000000) # 2ns
	finalize_simulation(newSim, shellFile, outputDir)

	# NPT production run
	newSim = SimGromacs([mdp.NPT, mdpFF], shellFile, 
				mdrun=mdrunCmd,
				mdpSuffix='NPT_sim',
				suffix='NPT_sim_'+str(i),
				coords=currentCoords)
	newSim.set_param('nsteps', 4000000) # 4ns
	finalize_simulation(newSim, shellFile, outputDir)

# Call box_resize.py
shellFile.write('\nsleep 1\n')
shellFile.write('python3 box_resize.py gmx '+'NPT_sim_'+str(n_runs-1)+' 3 gro_interface_start.gro\nsleep 1\n')
currentCoords = 'gro_interface_start.gro'

# NVT simulation with interface (for surface tension)
newSim = SimGromacs([mdpFF, mdp.NVT_interface_PMEVdW], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVT_interface',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 10000000) 
#finalize_simulation(newSim, shellFile, outputDir)