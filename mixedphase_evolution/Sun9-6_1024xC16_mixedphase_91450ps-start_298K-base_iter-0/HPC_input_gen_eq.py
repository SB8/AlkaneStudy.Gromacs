
import sys, os

# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_eq.sh'

currentCoords = 'Sun9-6_1024xC16_240-340K_41450ps.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gmx mdrun'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '7:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.COMPASS_LINCS

mdp_NPT = dict(mdp.NPT)

# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# Eq
Teq = 298
newSim = SimGromacs([mdpFF, dict(mdp.NVT_eq)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVT_eq_'+str(Teq)+'K',
			traj='xtc',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-temp', Teq)
newSim.set_param('nsteps', 100000) # 100 ps
newSim.set_param('nstxout-compressed', 100)
finalize_simulation(newSim, shellFile, outputDir)


newSim = SimGromacs([mdpFF, dict(mdp.NPT_eq)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq_'+str(Teq)+'K',
			traj='xtc',
			table='table6-9.xvg',
			coords=currentCoords)
#currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-vel', 'no')
newSim.set_param('nsteps', 1000000) # 1 ns
newSim.set_param('nstxout-compressed', 1000)
finalize_simulation(newSim, shellFile, outputDir)


