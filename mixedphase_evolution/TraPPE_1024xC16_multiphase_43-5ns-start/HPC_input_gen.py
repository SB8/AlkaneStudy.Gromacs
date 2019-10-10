
import sys, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-Tlist')
parser.add_argument('-iter')
args = parser.parse_args()

# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs_'+args.Tlist+'K_'+args.iter+'.sh'
currentCoords = 'gro_NPTeq_280K_100ps_multiphase.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gmx mdrun'

# Strings to replace in shell header
pbsVars = {'ncpus': '48', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.TraPPE
mdpFF['coulombtype'] = 'Cut-off' # No charges

mdp_NPT = dict(mdp.NPT)
mdp_NPT['nstxout-compressed'] = '5000' # 1 frame per 10ps, 1000 frames in 10ns sim

# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# Eq
Teq = 280
newSim = SimGromacs([mdpFF, mdp.NPT_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq_'+str(Teq),
			traj=['xtc', 'trr'],
			coords=currentCoords)
#currentCoords = newSim.coordsOut
newSim.set_param('ref-t', Teq)
newSim.set_param('gen-temp', Teq)
newSim.set_param('nstxout', 1000) # Needed for trr
newSim.set_param('nstvout', 1000)
newSim.set_param('nsteps', 500000) # 100 ps
#finalize_simulation(newSim, shellFile, outputDir)

#= T scan
for T in args.Tlist.split(','):
	newSim = SimGromacs([mdpFF, mdp_NPT], shellFile, 
				mdrun=mdrunCmd,
				mdpSuffix='NPT_'+T+'K',
				suffix='NPT_'+T+'K'+'_'+args.iter,
				coords='gro_NPT_'+T+'K'+'_'+str(int(args.iter)-1)+'.gro')
	# Coordinate filename shouldn't be overwritten 
	newSim.set_param('ref-t', T)
	newSim.set_param('nsteps', 5000000) # 10 ns
	finalize_simulation(newSim, shellFile, outputDir)

shellFile.close()

