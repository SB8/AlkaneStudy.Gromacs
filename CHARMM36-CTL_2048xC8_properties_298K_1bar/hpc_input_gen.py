
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '2048xC8_AA_start.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.CHARMM36

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
newSim.set_param('constraints', 'none') 
# This stores the filename of the current coordinate file (.gro)
currentCoords = newSim.coordsOut
# Write EM to file
finalize_simulation(newSim, shellFile, outputDir)

# Equilibration at atmospheric pressure
newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 4000000)
finalize_simulation(newSim, shellFile, outputDir)

# NPT production run
newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_sim', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 10000000) 
finalize_simulation(newSim, shellFile, outputDir)

# Call box_resize.py
shellFile.write('\nsleep 1\n')
shellFile.write('python3 box_resize.py gmx '+currentCoords+' 3 gro_interface_start.gro\nsleep 1\n')
currentCoords = 'gro_interface_start.gro'

# NVT simulation with interface (for surface tension)
newSim = SimGromacs([mdpFF, mdp.NVT_interface_PMEVdW], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVT_interface', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 10000000) 
finalize_simulation(newSim, shellFile, outputDir)
