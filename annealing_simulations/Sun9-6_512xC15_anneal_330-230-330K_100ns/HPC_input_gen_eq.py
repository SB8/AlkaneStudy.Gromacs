
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

currentCoords = '512xC15_AA_start.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '72', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.COMPASS_LINCS

# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir, 'run_gromacs_eq.sh'), 'w', newline='\n')

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
			table='table6-9.xvg',
			coords=currentCoords)
# This stores the filename of the current coordinate file (.gro)
currentCoords = newSim.coordsOut
# Write EM to file
finalize_simulation(newSim, shellFile, outputDir)


# Equilibration at atmospheric pressure (using gen-vel = yes)
newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
			mdrun=mdrunCmd,
			mdpSuffix='NPT_eq',
			suffix='NPT_eq',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 2000000) # 2ns
newSim.set_param('ref-t', 330)
finalize_simulation(newSim, shellFile, outputDir)

