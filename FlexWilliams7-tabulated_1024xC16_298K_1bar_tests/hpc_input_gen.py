
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_unbuffered.sh'
currentCoords = '1024xC16-AA_5nsEq-FlexWilliams.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.FlexWilliams
mdpFF['energygrps'] = 'C H' # Energy groups needed to read separate buckingham potential tables
mdpFF['energygrp-table'] = 'C C C H H H'
mdpFF['vdwtype'] = 'User'

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# NPT production run
newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_sim_unbuff_1E-3spacing',
			coords=currentCoords,
			topol='topol.top',
			table='table.xvg',
			indexFile='index.ndx')
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 5000000) 
finalize_simulation(newSim, shellFile, outputDir)
