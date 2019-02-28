
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '1024xC16_2nsEq-L-OPLS.gro'
mdrunCmd = 'gmx mdrun'

anneal_temps = [340, 240, 340]

# Set force field parameters
mdpFF = mdp.L_OPLS
# Params for annealing (start from NPT)
mdp_anneal = dict(mdp.NPT)
mdp_anneal['annealing'] = 'periodic'
mdp_anneal['annealing-npoints'] = '3'
mdp_anneal['annealing-time'] = '0 50000 100000' # ps
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))
mdp_anneal['nstxout-compressed'] = '25000' # 1 frame = 0.1K, 2000 frames total

# Open shell script for writing
shellFile = open(os.path.join(outputDir,shellName), 'w')

# Energy minimization
#newSim = SimGromacs([mdpFF, mdp.EM], shellFile, 
#			mdrun=mdrunCmd,
#			suffix='EM', 
#			traj='trr',
#			coords=currentCoords)
# This stores the filename of the current coordinate file (.gro)
#currentCoords = newSim.coordsOut
# Write EM to file
#finalize_simulation(newSim, shellFile, outputDir)

# Equilibration at atmospheric pressure
#newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
#			mdrun=mdrunCmd,
#			suffix='NPT_eq', 
#			coords=currentCoords)
#currentCoords = newSim.coordsOut
#newSim.set_param('nsteps', 2000000) 
#finalize_simulation(newSim, shellFile, outputDir)

# Simulated annealing, cycle 1
newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K_1', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 50000000) # 100ns
finalize_simulation(newSim, shellFile, outputDir)

# Cycle 2
#newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
#			mdrun=mdrunCmd,
#			suffix='NPT_anneal_340-240-340K_2', 
#			coords=currentCoords)
#currentCoords = newSim.coordsOut
#newSim.set_param('nsteps', 50000000)
#finalize_simulation(newSim, shellFile, outputDir)
