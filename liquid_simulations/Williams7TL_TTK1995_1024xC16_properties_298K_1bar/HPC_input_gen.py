
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '1024xC16-AA_5nsEq_FlexWilliams.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.WilliamsTabLincs)

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
			table='table.xvg',
			indexFile='index.ndx',
			coords=currentCoords)
# This stores the filename of the current coordinate file (.gro)
coordsEM = newSim.coordsOut
# Write EM to file
finalize_simulation(newSim, shellFile, outputDir)

n_runs = 3

for i in range(0, n_runs, 1):

	# Equilibration at atmospheric pressure (using gen-vel = yes)
	newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
				mdrun=mdrunCmd,
				mdpSuffix='NPT_eq',
				suffix='NPT_eq_'+str(i),
				table='table.xvg',
				indexFile='index.ndx',
				coords=coordsEM)
	currentCoords = newSim.coordsOut
	newSim.set_param('nsteps', 2000000) # 2ns
	finalize_simulation(newSim, shellFile, outputDir)

	# NPT production run
	newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
				mdrun=mdrunCmd,
				mdpSuffix='NPT_sim',
				suffix='NPT_sim_'+str(i),
				table='table.xvg',
				indexFile='index.ndx',
				coords=currentCoords)
	newSim.set_param('nsteps', 4000000) # 4ns
	finalize_simulation(newSim, shellFile, outputDir)

