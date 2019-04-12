
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join(os.pardir, 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

currentCoords = '1024xC16_4nsEq-FW7L_shiftCC-0.017'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.FlexWilliamsLincs
mdpFF['vdwtype'] = 'User' # Use tabulated potential
mdpFF['energygrps'] = 'C H'
mdpFF['energygrp-table'] = 'C H H H'

# Params for annealing (start from NPT)
mdp_anneal = dict(mdp.NPT)
mdp_anneal['annealing'] = 'single'
mdp_anneal['annealing-npoints'] = '2'
mdp_anneal['annealing-time'] = '0 50000' # ps
mdp_anneal['nsteps'] = '50000000' # 50ns - 1fs time step!
mdp_anneal['nstxout-compressed'] = '50000' # 1 frame = 0.1K, 1000 frames each half

# Simulated annealing, decreasing T
shellFile = open(os.path.join(outputDir, 'run_gromacs_cooling.sh'), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

T_m = 290
anneal_temps = [T_m+50, T_m-50]
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			table='table.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()

# Simulated annealing, increasing T
shellFile = open(os.path.join(outputDir, 'run_gromacs_heating.sh'), 'w', newline='\n')

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

anneal_temps = [T_m-50, T_m+50]
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			table='table.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()
