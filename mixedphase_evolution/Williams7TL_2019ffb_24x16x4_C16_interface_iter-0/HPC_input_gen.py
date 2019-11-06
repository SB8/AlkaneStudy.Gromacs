
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = 'gro_NP6T_306K.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3_err-null.sh')
print('Using base shell script: ', hpcHeader)
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '23:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.WilliamsTabLincs)

iter = 0
n_parts = 1
Tbase = 310
Tlist = [Tbase-12, Tbase-6, Tbase, Tbase+6]
dt = float(mdpFF['dt'])

# NP3T
totaltime = 10 # ns
mdpNPT = dict(mdp.NPT)
mdpNPT['Pcoupltype'] = 'anisotropic'
mdpNPT['compressibility'] = '5.0e-5 5.0e-5 5.0e-5 5.0e-5 5.0e-5 5.0e-5'
mdpNPT['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdpNPT['nsteps'] = str(int(1E3*totaltime/dt))
mdpNPT['nstxout-compressed'] = str(int(totaltime/dt)) # 100 steps


runsperpart = int(len(Tlist)/n_parts)

for i in range(n_parts):

	TlistPart = Tlist[i*runsperpart:(i+1)*runsperpart]
	Tstring = '-'.join([str(i) for i in TlistPart])
	shellName = 'run_gromacs_'+Tstring+'K_iter'+str(iter)+'_part'+str(i)+'.sh'
	shellFile = open(os.path.join(outputDir,shellName), 'w', newline='\n')

	# Write HPC header file (with job description)
	for line in open(hpcHeader):
		for var, rep in pbsVars.items():
			line = line.replace(var, rep)
		
		shellFile.write(line)

	# Temperature loop
	for T in Tlist:
		mdpNPT['ref-t'] = str(T)
		newSim = SimGromacs([mdpFF, mdpNPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NP3T_'+str(T)+'K_'+'{:.1f}'.format(totaltime)+'ns_iter'+str(iter),
				table='table.xvg',
				indexFile='index.ndx',
				coords=currentCoords)
		finalize_simulation(newSim, shellFile, outputDir)
