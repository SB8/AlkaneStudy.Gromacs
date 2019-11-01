
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = 'C16_UA_24x18x4_s2x0x0.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '48', 'walltime': '23:00:00', 'budgetname': 'QMUL_BURROWS'}


# Set force field parameters
mdpFF = dict(mdp.PYSW)

Teq = 360
Tplus = 317

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)
	
	shellFile.write(line)

# NVT melting at high temperature with 2xEps
mdpNVTeq = dict(mdp.NVT_eq)
mdpNVTeq['ref-t'] = str(Teq)
mdpNVTeq['gen-temp'] = str(Teq)
mdpNVTeq['nsteps'] = '2000000'
mdpNVTeq['nstxout-compressed'] = '2000'

newSim = SimGromacs([mdpFF, mdpNVTeq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVTeq_2xEps_'+str(Teq)+'K',
			topol='topol_2xEps.top',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# NPT Tmax -> T+ with 2xEps
mdpNPTeq = dict(mdp.NPT_eq)
mdpNPTeq['ref-t'] = str(Tplus)
mdpNPTeq['gen-vel'] = 'no'
mdpNPTeq['Pcoupltype'] = 'anisotropic'
mdpNPTeq['compressibility'] = '5.0e-5 5.0e-5 5.0e-5 0.0 0.0 0.0' # Fix angles, vary lengths
mdpNPTeq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
#mdpNPTeq['refcoord_scaling'] = 'all'
mdpNPTeq['nsteps'] = '1000000'
mdpNPTeq['nstxout-compressed'] = '1000'

newSim = SimGromacs([mdpFF, mdpNPTeq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPTeq_2xEps_'+str(Tplus)+'K',
			topol='topol_2xEps.top',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)

# NPT Equilibration at T+ without 2xEps
mdpNPT2 = dict(mdp.NPT_eq)
mdpNPT2['ref-t'] = str(Tplus)
mdpNPT2['gen-vel'] = 'no'
#mdpNPT2['tau-p'] = '4.0'
mdpNPT2['Pcoupltype'] = 'anisotropic'
mdpNPT2['compressibility'] = '5.0e-5 5.0e-5 5.0e-5 5.0e-5 5.0e-5 5.0e-5' # FULL aniso
mdpNPT2['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdpNPT2['nsteps'] = '1000000'
mdpNPT2['nstxout-compressed'] = '1000'

newSim = SimGromacs([mdpFF, mdpNPT2], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_'+str(Tplus)+'K',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
