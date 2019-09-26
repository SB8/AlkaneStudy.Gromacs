
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = 'C16_18x18x4.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = mdp.CHARMM36

mdp_eq = mdp.NPT_eq # eq to generate velocities
# Anisotropic pressure coupling
mdp_eq['nsteps'] = '2000000'
mdp_eq['Pcoupltype'] = 'anisotropic'
mdp_eq['compressibility'] = '5e-5 5e-5 5e-5 0.0 0.0 0.0' # xx, yy, zz, xy/yx, xz/zx and yz/zy
mdp_eq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'

mdp_anneal = mdp.NPT
# Anisotropic pressure coupling
mdp_anneal['Pcoupltype'] = 'anisotropic'
mdp_anneal['compressibility'] = '5e-5 5e-5 5e-5 0.0 0.0 0.0' # xx, yy, zz, xy/yx, xz/zx and yz/zy
mdp_anneal['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdp_anneal['tau-p'] = '4.0'
# Annealing
mdp_anneal['annealing'] = 'single'
mdp_anneal['annealing-npoints'] = '3'
mdp_anneal['annealing-time'] = '0 10000 20000' # ps
mdp_anneal['nsteps'] = '20000000' # 20ns - 1fs time step!
mdp_anneal['nstxout-compressed'] = '10000' # 1000 frames each half, 2000 in total

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


T_m = 291
anneal_temps = [T_m-40, T_m+10, T_m-40]

# Equilibration
mdp_eq['ref-t'] = str(anneal_temps[0])
mdp_eq['gen-temp'] = str(anneal_temps[0])

newSim = SimGromacs([mdpFF, mdp_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_eq',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# Annealing
mdp_anneal['ref-t'] = str(anneal_temps[0]) # Shouldn't matter
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()
