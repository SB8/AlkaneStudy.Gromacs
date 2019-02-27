
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
groStart = '1024xC16-AA_2nsEq.gro'
mdrunCmd = 'gmx mdrun'

# Set force field parameters
mdpFF = mdp.L_OPLS

# Open shell script for writing
shellFile = open(os.path.join(outputDir,shellName), 'w')

# NPT simulation
newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_sim', 
			coords=groStart)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 500000) 
finalize_simulation(newSim, shellFile, outputDir)
