
import sys, os

# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_eq.sh'
#shellName = 'run_gromacs_'+args.Tlist+'K_'+args.iter+'.sh'

currentCoords = 'PYS_1024xC16_240-340K_40900ps.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gmx mdrun'

# Strings to replace in shell header
pbsVars = {'ncpus': '72', 'walltime': '7:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.PYSW

mdp_NPT = dict(mdp.NPT)

# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# Eq
Teq = 290
newSim = SimGromacs([mdpFF, dict(mdp.NVT_eq)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVT_eq_'+str(Teq)+'K',
			traj='xtc',
			coords=currentCoords)
currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-temp', Teq)
newSim.set_param('nsteps', 50000) # 100 ps
newSim.set_param('nstxout-compressed', 50)
finalize_simulation(newSim, shellFile, outputDir)


newSim = SimGromacs([mdpFF, dict(mdp.NPT_eq)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq_'+str(Teq)+'K',
			traj=['xtc', 'trr'],
			coords=currentCoords)
#currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-vel', 'no')
newSim.set_param('nstxout', 5000) # Needed for trr
newSim.set_param('nstvout', 5000)
newSim.set_param('nsteps', 500000) # 1 ns
newSim.set_param('nstxout-compressed', 500)
finalize_simulation(newSim, shellFile, outputDir)


