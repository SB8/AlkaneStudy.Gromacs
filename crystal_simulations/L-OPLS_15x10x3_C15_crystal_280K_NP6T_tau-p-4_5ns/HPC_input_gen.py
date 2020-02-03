
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
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

T = 280

# Set force field parameters
mdpFF = dict(mdp.L_OPLS)

mdp_eq = dict(mdp.NPT_eq) # eq to generate velocities
# Anisotropic pressure coupling
mdp_eq['nsteps'] = '1000000'
mdp_eq['Pcoupltype'] = 'anisotropic'
mdp_eq['compressibility'] = '5e-5 5e-5 5e-5 0.0 0.0 0.0' # xx, yy, zz, xy/yx, xz/zx and yz/zy
mdp_eq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdp_eq['ref-t'] = str(T)
mdp_eq['gen-temp'] = str(T)

mdp_NP6T = dict(mdp.NPT)
mdp_NP6T['nsteps'] = '2500000'
mdp_NP6T['nstxout-compressed'] = '2500'
mdp_NP6T['Pcoupltype'] = 'anisotropic'
mdp_NP6T['compressibility'] = '5e-5 5e-5 5e-5 5e-5 5e-5 5e-5' # xx, yy, zz, xy/yx, xz/zx and yz/zy
mdp_NP6T['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdp_NP6T['tau-p'] = '4.0'
mdp_NP6T['ref-t'] = str(T)

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
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# NP6T
newSim = SimGromacs([mdpFF, mdp_NP6T], shellFile, 
			mdrun=mdrunCmd,
			suffix='NP6T_'+str(T)+'K',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()