
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '2048xC8-AA_5nsEq-CHARMM36.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.FlexWilliamsLincs
mdpFF['vdwtype'] = 'User' # Use tabulated potential
mdpFF['energygrps'] = 'C H'
mdpFF['energygrp-table'] = 'C H H H'

shiftStrs = ['0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022', '0.024', '0.026', '0.028', '0.030']

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
			topol='topol_'+shiftStrs[0]+'.top',
			indexFile='index.ndx',
			table='tables/table_'+shiftStrs[0]+'.xvg',
			coords=currentCoords)
# This stores the filename of the current coordinate file (.gro)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# Equilibration at atmospheric pressure
newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq',
			topol='topol_'+shiftStrs[0]+'.top',
			indexFile='index.ndx',
			table='tables/table_'+shiftStrs[0]+'.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 2000000)
finalize_simulation(newSim, shellFile, outputDir)

for shift in shiftStrs:

	tableFile = 'tables/table_'+shift+'.xvg' # Unix path since running on HPC

	# NPT production run
	newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPT_sim_'+shift,
				mdpSuffix='NPT_sim',
				topol='topol_'+shift+'.top',
				indexFile='index.ndx',
				table=tableFile,
				coords=currentCoords)
	currentCoords = newSim.coordsOut
	newSim.set_param('nsteps', 4000000) 
	finalize_simulation(newSim, shellFile, outputDir)
