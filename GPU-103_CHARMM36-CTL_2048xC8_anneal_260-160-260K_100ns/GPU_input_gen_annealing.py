
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_GPU.sh'
currentCoords = '2048xC8-AA.gro' 
mdrunCmd = 'gmx mdrun'

# Set force field parameters
mdpFF = mdp.CHARMM36
# Params for annealing (start from NPT)
mdp_anneal = dict(mdp.NPT)
mdp_anneal['annealing'] = 'single'
mdp_anneal['annealing-npoints'] = '2'
mdp_anneal['annealing-time'] = '0 50000' # ps
mdp_anneal['nsteps'] = '50000000' # 50ns - 1fs time step!
mdp_anneal['nstxout-compressed'] = '50000' # 1 frame = 0.1K, 1000 frames each half

shellFile = open(os.path.join(outputDir,shellName), 'w')

# Simulated annealing, decreasing T
T_m = 210 # Rounded down
anneal_temps = [T_m+50, T_m-50]
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# increasing T
anneal_temps = [T_m-50, T_m+50]
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()
