
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
groStart = '2048xC7_UA_start.gro'
hpcHeader = 'MMM_header_2016-3.sh' 
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '72', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.PYSW

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w')

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
newSim.set_param('nsteps', 1000000)
finalize_simulation(newSim, shellFile, outputDir)

# NPT production run
newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_sim', 
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('nsteps', 1000000) 
finalize_simulation(newSim, shellFile, outputDir)

# cos-acceleration (viscosity) sim
base_acc = 0.01
base_nsteps = 4000000
f = 2**0.5
extrapoints = [4,2] # Below and above
acc = base_acc/f**extrapoints[0]

for i in range(1+sum(extrapoints)):
	newSim = SimGromacs([mdpFF, mdp.NPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPT_cosacc_'+'{:.4f}'.format(acc),
				coords=currentCoords)
	currentCoords = newSim.coordsOut
	newSim.set_param('nsteps', int((base_nsteps+1)*base_acc/acc/100000)*100000)
	newSim.set_param('nstcalcenergy', 10) 
	newSim.set_param('nstenergy', 100) 
	newSim.set_param('cos-acceleration', '{:.6f}'.format(acc))
	newSim.set_param('nstxout-compressed', 10000) # Trajectory less important
	finalize_simulation(newSim, shellFile, outputDir)
	acc *= f