
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'GPU_run_gromacs.sh'
groStart = '1024xC16-AA_start.gro'
mdrunCmd = 'gmx mdrun'

# Set force field parameters
mdpFF = mdp.L_OPLS
# Params for NPT
mdp_NPT = mdp.NPT
# Params for annealing (start from NPT)
mdp_anneal = dict(mdp_NPT)
mdp_anneal['annealing'] = 'periodic'
mdp_anneal['annealing-npoints'] = '3'
mdp_anneal['annealing-time'] = '0 50000 100000' # ps
mdp_anneal['annealing-temp'] = '340 240 340'
mdp_anneal['nstxout-compressed'] = '10000' # Less often due to large number of steps

# Open shell script for writing
shellFile = open(os.path.join(outputDir,shellName), 'w')

# Energy minimization
newSim = SimGromacs([mdpFF, mdp.EM], shellFile, 
			mdrun=mdrunCmd,
			suffix='EM', 
			traj='trr',
			coords=groStart)
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
newSim.set_param('nsteps', 3000000) 
finalize_simulation(newSim, shellFile, outputDir)

# Simulated annealing
# Cycle 1
newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_340-240-340K_cycle1', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 50000000) # 100ns
finalize_simulation(newSim, shellFile, outputDir)
# Cycle 2
newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_340-240-340K_cycle2', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 50000000)
finalize_simulation(newSim, shellFile, outputDir)
