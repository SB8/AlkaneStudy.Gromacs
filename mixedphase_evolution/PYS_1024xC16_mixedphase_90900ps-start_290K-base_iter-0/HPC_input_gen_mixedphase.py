
import sys, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-Tlist')
parser.add_argument('-Tstart')
parser.add_argument('-iter')
args = parser.parse_args()

# User numerical types here, convert to strings after if needed
Tstart = 290 # int(args.Tstart)
iter = 0 # int(args.iter)
if iter == 0:
	Tlist = [Tstart-6, Tstart, Tstart+6, Tstart+12]

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

currentCoords = 'gro_NPT_eq_290K.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gmx mdrun'

# Strings to replace in shell header
pbsVars = {'ncpus': '72', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.PYSW)

mdp_NPT = dict(mdp.NPT)
mdp_NPT['nstxout-compressed'] = '10000' # 1000 frames
mdp_NPT['tau-p'] = '4.0'
mdp_NPT['nsteps'] = '10000000' # 20 ns


# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)


#= T scan
for T in Tlist:
	if iter == 0:
		# Start from eq config
		coordsStr = currentCoords
		# Set annealing parameters to avoid temperature discontinuity
		mdp_NPT['annealing'] = 'single'
		mdp_NPT['annealing-npoints'] = '3'
		mdp_NPT['annealing-time'] = '0 4000 20000' # ps
		mdp_NPT['annealing-temp'] = str(Tstart)+' '+str(T)+' '+str(T)
		mdp_NPT['ref-t'] = str(T) # Shouldn't matter 

	else:
		# Start from previous configuration
		coordsStr = 'gro_NPT_'+str(T)+'K'+'_'+str(iter-1)+'.gro'
		mdp_NPT['ref-t'] = str(Tstart)
		
	
	newSim = SimGromacs([mdpFF, mdp_NPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPT_'+str(T)+'K'+'_'+str(iter), # Has to match coordsStr set above
				coords=coordsStr)
	finalize_simulation(newSim, shellFile, outputDir)

shellFile.close()

