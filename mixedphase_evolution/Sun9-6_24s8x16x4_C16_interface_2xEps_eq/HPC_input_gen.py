
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = 'C16_24x16x4_solid8_add2x0x0.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3_err-null.sh')
print('Using base shell script: ', hpcHeader)
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '23:00:00', 'budgetname': 'QMUL_BURROWS'}


# Set force field parameters
mdpFF = dict(mdp.COMPASS_LINCS)

Teq = 360
Tplus = 313
dt = float(mdpFF['dt'])

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)

	shellFile.write(line)

# EM
newSim = SimGromacs([mdpFF, mdp.EM], shellFile, 
			mdrun=mdrunCmd,
			suffix='EM_2xEps_'+str(Teq)+'K',
			topol='topol_2xEps.top',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
#finalize_simulation(newSim, shellFile, outputDir)

# NVT melting at high temperature with 2xEps
totaltime = 4 # ns
mdpNVTeq = dict(mdp.NVT_eq)
mdpNVTeq['ref-t'] = str(Teq)
mdpNVTeq['gen-temp'] = str(Teq)
mdpNVTeq['nsteps'] = str(int(1E3*totaltime/dt))
mdpNVTeq['nstxout-compressed'] = str(int(totaltime/dt)) # 1000 steps

newSim = SimGromacs([mdpFF, mdpNVTeq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NVTeq_2xEps_'+str(Teq)+'K',
			topol='topol_2xEps.top',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
#finalize_simulation(newSim, shellFile, outputDir)

# NPT Tmax -> T+ with 2xEps
totaltime = 0.5 # ns
mdpNPTeq = dict(mdp.NPT_eq)
mdpNPTeq['ref-t'] = str(Tplus)
mdpNPTeq['gen-vel'] = 'no'
mdpNPTeq['Pcoupltype'] = 'anisotropic'
mdpNPTeq['compressibility'] = '5.0e-5 5.0e-5 5.0e-5 0.0 0.0 0.0'
mdpNPTeq['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdpNPTeq['nsteps'] = str(int(1E3*totaltime/dt))
mdpNPTeq['nstxout-compressed'] = str(int(totaltime/dt))

newSim = SimGromacs([mdpFF, mdpNPTeq], shellFile, 
			mdrun=mdrunCmd,
			suffix='NP3T_2xEps_'+str(Tplus)+'K',
			topol='topol_2xEps.top',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
#finalize_simulation(newSim, shellFile, outputDir)

# NPT Equilibration at T+ without 2xEps
totaltime = 1 # ns
mdpNPT2 = dict(mdp.NPT_eq)
mdpNPT2['ref-t'] = str(Tplus)
mdpNPT2['gen-vel'] = 'no'
mdpNPT2['Pcoupltype'] = 'anisotropic'
mdpNPT2['compressibility'] = '5.0e-5 5.0e-5 5.0e-5 5.0e-5 5.0e-5 5.0e-5' # FULL aniso
mdpNPT2['ref-p'] = '1.0 1.0 1.0 0.0 0.0 0.0'
mdpNPT2['nsteps'] = str(int(1E3*totaltime/dt))
mdpNPT2['nstxout-compressed'] = str(int(totaltime/dt))

newSim = SimGromacs([mdpFF, mdpNPT2], shellFile, 
			mdrun=mdrunCmd,
			suffix='NP6T_'+str(Tplus)+'K',
			table='table6-9.xvg',
			coords=currentCoords)
currentCoords = newSim.coordsOut
finalize_simulation(newSim, shellFile, outputDir)
