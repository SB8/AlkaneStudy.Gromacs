
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_GPU.sh'
currentCoords = '512xC16-AA_2nsEq_CHARMM36.gro'
mdrunCmd = 'gmx mdrun'

# Set force field parameters
mdpFF = mdp.CHARMM36

# Params for annealing (start from NPT)
mdp_anneal = dict(mdp.NPT)
mdp_anneal['annealing'] = 'single'
mdp_anneal['annealing-npoints'] = '2'
mdp_anneal['annealing-time'] = '0 50000' # ps
mdp_anneal['nsteps'] = '50000000' # 50ns - 1fs time step for CHARMM36
mdp_anneal['nstxout-compressed'] = '50000' # 1000 frames each half
mdp_anneal['nstxout'] = '50000'
mdp_anneal['nstvout'] = '50000'
mdp_anneal['nstfout'] = '50000'


# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

T_m = 280
# decreasing T
anneal_temps = [T_m+50, T_m-50]
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			traj=['xtc', 'trr'],
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# increasing T
anneal_temps = [T_m-50, T_m+50]
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			traj=['xtc', 'trr'],
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()