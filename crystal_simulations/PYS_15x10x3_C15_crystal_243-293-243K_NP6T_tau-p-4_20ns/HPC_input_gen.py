
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = 'C15-UA_15x10x3_Pbcm.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '48', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.PYSW)

mdp_NP3T_eq = dict(mdp.NPT_eq) # eq to generate velocities
# Anisotropic pressure coupling
mdp_NP3T_eq['nsteps'] = '1000000' # 2fs time step
mdp_NP3T_eq['Pcoupltype'] = 'anisotropic'
mdp_NP3T_eq['compressibility'] = '5e-5 5e-5 5e-5 0.0 0.0 0.0'
mdp_NP3T_eq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'

mdp_NP6T_eq = dict(mdp.NPT_eq)
mdp_NP6T_eq['nsteps'] = '1000000' # 2fs time step
mdp_NP6T_eq['Pcoupltype'] = 'anisotropic'
mdp_NP6T_eq['compressibility'] = '5e-5 5e-5 5e-5 5e-5 5e-5 5e-5'
mdp_NP6T_eq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'

mdp_anneal = dict(mdp.NPT)
mdp_anneal['Pcoupltype'] = 'anisotropic'
mdp_anneal['compressibility'] = '5e-5 5e-5 5e-5 5e-5 5e-5 5e-5'
mdp_anneal['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdp_anneal['tau-p'] = '4.0'
# Annealing - UA SETTINGS
mdp_anneal['annealing'] = 'single'
mdp_anneal['annealing-npoints'] = '3'
mdp_anneal['annealing-time'] = '0 10000 20000' # ps
mdp_anneal['nsteps'] = '10000000' # 20ns - 2fs time step!
mdp_anneal['nstxout-compressed'] = '5000' # 1000 frames each half, 2000 in total

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
#finalize_simulation(newSim, shellFile, outputDir)


T_m = 283
anneal_temps = [T_m-40, T_m+10, T_m-40]

# Equilibration
mdp_NP3T_eq['ref-t'] = str(anneal_temps[0])
mdp_NP3T_eq['gen-temp'] = str(anneal_temps[0])

newSim = SimGromacs([mdpFF, mdp_NP3T_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NP3T_eq',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

mdp_NP6T_eq['ref-t'] = str(anneal_temps[0])
mdp_NP6T_eq['gen-vel'] = 'no'

newSim = SimGromacs([mdpFF, mdp_NP6T_eq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NP6T_eq',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

for taup in [8,6,4,2]:
	mdp_NP6T = dict(mdp.NPT)
	mdp_NP6T['Pcoupltype'] = 'anisotropic'
	mdp_NP6T['compressibility'] = '5e-5 5e-5 5e-5 5e-5 5e-5 5e-5'
	mdp_NP6T['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
	mdp_NP6T['ref-t'] = str(anneal_temps[0])
	mdp_NP6T['tau-p'] = str(taup)
	mdp_NP6T['nsteps'] = '500000'

	newSim = SimGromacs([mdpFF, mdp_NP6T], shellFile, 
				mdrun=mdrunCmd,
				suffix='NP6T_tau-p-'+str(taup)+'_K',
				coords=currentCoords)
	finalize_simulation(newSim, shellFile, outputDir)
	#currentCoords = newSim.coordsOut




# Annealing
mdp_anneal['ref-t'] = str(anneal_temps[0]) # Shouldn't matter
mdp_anneal['annealing-temp'] = ' '.join(map(str,anneal_temps))

newSim = SimGromacs([mdpFF, mdp_anneal], shellFile, 
			mdrun=mdrunCmd,
			suffix='NP6T_anneal_'+'-'.join(map(str,anneal_temps))+'K',
			coords=currentCoords)
currentCoords = newSim.coordsOut
#finalize_simulation(newSim, shellFile, outputDir)
shellFile.close()
