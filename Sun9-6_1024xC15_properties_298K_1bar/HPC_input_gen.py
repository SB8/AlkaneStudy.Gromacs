
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '1024xC15-AA_3nsEq-CHARMM36.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.COMPASS
mdpFF['constraints'] = 'h-bonds'
mdpFF['constraint-algorithm'] = 'Lincs'

mdpInterface = dict(mdp.NVT) # Longer cutoffs for interface sim
mdpInterface['rlist'] = '1.3'
mdpInterface['rcoulomb'] = '1.3'
mdpInterface['rvdw'] = '1.2'
mdpInterface['DispCorr'] = 'no'

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# Equilibration at atmospheric pressure
newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq', 
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 4000000)
finalize_simulation(newSim, shellFile, outputDir)

# NPT production run
newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_sim',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 10000000) 
finalize_simulation(newSim, shellFile, outputDir)

# Call box_resize.py
shellFile.write('\nsleep 1\n')
shellFile.write('python3 box_resize.py gmx '+newSim.suffix+' 3 gro_interface_start.gro\nsleep 1\n')
currentCoords = 'gro_interface_start.gro'

# NVT simulation with interface (for surface tension)
newSim = SimGromacs([mdpFF, mdpInterface], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVT_interface',
			table='table6-9.xvg', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 10000000) 
finalize_simulation(newSim, shellFile, outputDir)
