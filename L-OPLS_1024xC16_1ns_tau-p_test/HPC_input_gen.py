import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '1024xC15-AA_14nsEq-FWL4_no-vel.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.L_OPLS

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

# NPT equilibration
newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 2000000) 
finalize_simulation(newSim, shellFile, outputDir)

# Loop over tau-p
for taup in [1, 2, 4, 8, 16]:

	newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPT_sim_taup_'+'{:.0f}'.format(taup), 
				coords=currentCoords)
	currentCoords = newSim.coordsOut
	newSim.set_param('tau-p', '{:.1f}'.format(taup)) 
	newSim.set_param('nsteps', 2000000) 
	finalize_simulation(newSim, shellFile, outputDir)
