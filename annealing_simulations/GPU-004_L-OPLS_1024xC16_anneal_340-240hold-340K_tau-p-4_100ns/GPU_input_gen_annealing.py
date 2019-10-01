
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_GPU.sh'
currentCoords = 'gro_NPT_anneal_340-240K.gro'
mdrunCmd = 'gmx mdrun'

# Set force field parameters
mdpFF = mdp.L_OPLS

# Params for annealing (start from NPT)
mdp_anneal = dict(mdp.NPT)
mdp_anneal['tau-p'] = '4.0' # For stability of pressure coupling in L-OPLS
mdp_anneal['annealing'] = 'single'
mdp_anneal['annealing-npoints'] = '2'
mdp_anneal['annealing-time'] = '0 50000' # ps
mdp_anneal['nsteps'] = '25000000' # 50ns - 2fs time step for L-OPLS
mdp_anneal['nstxout-compressed'] = '25000' # 1000 frames each half
mdp_anneal['nstxout'] = '25000'
mdp_anneal['nstvout'] = '25000'
mdp_anneal['nstfout'] = '25000'


# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

T_m = 290
# hold at Tm-50 (Easier to use annealing mdp even though both temps are the same)
anneal_temps = [T_m-50, T_m-50]
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