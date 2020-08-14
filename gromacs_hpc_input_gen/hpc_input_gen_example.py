
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.getcwd()
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
import cluster_dicts as cluster
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

# Set HPC cluster
hpc = dict(cluster.apocrita_sdv)
hpcHeader = os.path.join(gmxModDir, hpc['header'])
mdrunCmd = hpc['mdrun']
print('Using base shell script: ', hpcHeader)

pbsVars = {'ncpus': '48', 'walltime': '24:0:0'}

shellName = 'run_gromacs.sh'
currentCoords = 'C15_15x10x3_Pbcm_rot90Y.gro'

# Set force field parameters
mdpFF = mdp.PYSW
mdpNPT = dict(mdp.NPT)
mdpNPT['ref-t'] = '300'

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
			coords=currentCoords)
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
newSim.set_param('nsteps', 1000000)
newSim.set_param('ref-t', 303) # For example
finalize_simulation(newSim, shellFile, outputDir)

# NPT production run
newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_sim', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 1000000) 
finalize_simulation(newSim, shellFile, outputDir)
