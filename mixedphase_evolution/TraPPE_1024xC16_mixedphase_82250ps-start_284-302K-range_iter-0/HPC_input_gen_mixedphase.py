
import sys, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-Tlist')
parser.add_argument('-Tstart')
parser.add_argument('-iter')
args = parser.parse_args()

# User numerical types here, convert to strings after if needed
Tstart = 302 # int(args.Tstart)
iter = 0 # int(args.iter)
if iter == 0:
	Tlist = [Tstart-18, Tstart-12, Tstart-6, Tstart]

# Optionally set from command line argument
#Tlist = [] # [float(i) for i in args.Tlist.split(',')]

# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

Tstring = '-'.join([str(i) for i in Tlist])
shellName = 'run_gromacs_'+Tstring+'K_'+str(iter)+'.sh'

startCoords = 'gro_240-340K_32250ps.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '48', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.TraPPE)
mdpFF['coulombtype'] = 'Cut-off' # No charges

# Set simulation lengths
mdp_NVT = dict(mdp.NVT)
mdp_NVT['gen-vel'] = 'yes'
mdp_NVT['gen-seed'] = '-1' # Pseudo-random seed
mdp_NVT['nstxout-compressed'] = '2000' # 1000 frames
mdp_NVT['nsteps'] = '2000000' # 4 ns

mdp_NPTeq = dict(mdp.NPT_eq)
mdp_NPTeq['gen-vel'] = 'no'
del mdp_NPTeq['gen-temp']
del mdp_NPTeq['gen-seed']
mdp_NPTeq['nstxout-compressed'] = '2000'
mdp_NPTeq['nsteps'] = '500000' # 1 ns


mdp_NPT = dict(mdp.NPT)
mdp_NPT['nstxout-compressed'] = '10000' # 1000 frames
mdp_NPT['tau-p'] = '4.0'
mdp_NPT['nsteps'] = '10000000' # 20 ns


# Write HPC header file (with job description)
shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# T scan
for T in Tlist:

	# Set temperatures
	mdp_NVT['ref-t'] = str(T)
	mdp_NVT['gen-temp'] = str(T)
	mdp_NPTeq['ref-t'] = str(T)
	mdp_NPT['ref-t'] = str(T)

	if iter == 0:

		# NVT eq
		newSim = SimGromacs([mdpFF, mdp_NVT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NVT_'+str(T)+'K',
				coords=startCoords)
		currentCoords = newSim.coordsOut
		finalize_simulation(newSim, shellFile, outputDir)

		# NPT eq
		newSim = SimGromacs([mdpFF, mdp_NPTeq], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPTeq_'+str(T)+'K',
				coords=currentCoords)
		currentCoords = newSim.coordsOut
		finalize_simulation(newSim, shellFile, outputDir)

	else:
		# Start from previous configuration
		currentCoords = 'gro_NPT_'+str(T)+'K'+'_'+str(iter-1)+'.gro'
		
	# Iteration
	newSim = SimGromacs([mdpFF, mdp_NPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPT_'+str(T)+'K'+'_'+str(iter),
				coords=currentCoords)
	finalize_simulation(newSim, shellFile, outputDir)

shellFile.close()

