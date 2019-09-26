
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = 'C15_15x10x3_Pbcm.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '23:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.L_OPLS
mdp_eq = mdp.NPT_eq
mdp_NPT = mdp.NPT

T = 280
mdp_eq['ref-t'] = str(T)
mdp_eq['gen-temp'] = str(T)
mdp_eq['Pcoupltype'] = 'anisotropic'
mdp_eq['compressibility'] = '5e-5 5e-5 5e-5 0.0 0.0 0.0' # xx, yy, zz, xy/yx, xz/zx and yz/zy
mdp_eq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'

mdp_NPT['ref-t'] = str(T)
mdp_NPT['Pcoupltype'] = 'anisotropic'
mdp_NPT['compressibility'] = '5e-5 5e-5 5e-5 0.0 0.0 0.0' # xx, yy, zz, xy/yx, xz/zx and yz/zy
mdp_NPT['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'

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
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)


# Equilibration
newSim = SimGromacs([mdpFF, mdp_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq',
			coords=currentCoords)
newSim.set_param('nsteps', 1000000) # 2ns
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

tau_p = [3,4,5,6,8,10]

for tau in tau_p:

	# NPT production run
	newSim = SimGromacs([mdpFF, mdp_NPT], shellFile, 
				mdrun=mdrunCmd,
				suffix='NPT_tau-p_'+str(tau),
				coords=currentCoords)
	currentCoords = newSim.coordsOut
	newSim.set_param('nsteps', 1000000) # 2ns
	newSim.set_param('tau-p', float(tau))
	finalize_simulation(newSim, shellFile, outputDir)

