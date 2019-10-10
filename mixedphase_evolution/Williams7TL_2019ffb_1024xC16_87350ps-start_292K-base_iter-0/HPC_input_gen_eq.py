
import sys, os

# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_eq.sh'

currentCoords = 'gro_240-340K_37350ps.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '72', 'walltime': '23:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.WilliamsTabLincs)

mdp_NPT = dict(mdp.NPT)

# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# Eq
Teq = 292
newSim = SimGromacs([mdpFF, dict(mdp.NVT_eq)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVT_eq_'+str(Teq)+'K',
			traj='xtc',
			table='table.xvg',
			indexFile='index.ndx',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-temp', Teq)
newSim.set_param('nsteps', 500000)
newSim.set_param('nstxout-compressed', 1000)
finalize_simulation(newSim, shellFile, outputDir)


newSim = SimGromacs([mdpFF, dict(mdp.NPT_eq)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq_'+str(Teq)+'K',
			traj='xtc',
			table='table.xvg',
			indexFile='index.ndx',
			coords=currentCoords)
#currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-vel', 'no')
newSim.set_param('nsteps', 500000)
newSim.set_param('nstxout-compressed', 1000)
finalize_simulation(newSim, shellFile, outputDir)


