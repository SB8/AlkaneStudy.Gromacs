
import sys, os
# Tell script directiory of HPC input gen module
gmxModDir = os.path.join('..', '..', 'gromacs_hpc_input_gen')
sys.path.append(gmxModDir)

# Load default mdp dictionaries, simulation class
import default_mdp_dicts as mdp
from sim_class import SimGromacs, finalize_simulation

outputDir = os.getcwd()

shellName = 'run_gromacs.sh'
currentCoords = '1024xC15-AA_12nsEq_L-OPLS.gro'
hpcHeader = os.path.join(gmxModDir, 'MMM_header_2016-3.sh')
mdrunCmd = 'gerun mdrun_mpi'

# Strings to replace in shell header
pbsVars = {'ncpus': '96', 'walltime': '48:00:00', 'budgetname': 'QMUL_BURROWS'}

# Set force field parameters
mdpFF = dict(mdp.L_OPLS)
mdpFF['tau-p'] = '4.0' # Add mdpFF after ensemble in mdp list to overwrite e.g. [mdp.NPT_eq, mdpFF]

# Open shell script for writing
shellFile = open(os.path.join(outputDir, shellName), 'w', newline='\n') # Must use unix line endings

# Write HPC header file (with job description)
for line in open(hpcHeader):
	for var, rep in pbsVars.items():
		line = line.replace(var, rep)

	shellFile.write(line)


# Wesbarnett, 2fs ts
newSim = SimGromacs([mdp.NPT, dict(mdpFF)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_wb_2fs',
			topol='wb_topol.top',
			coords=currentCoords)
newSim.set_param('nsteps', 2000000) # 4ns
newSim.set_param('dt', 0.002)
newSim.set_param('define', '-DLOPLS')
finalize_simulation(newSim, shellFile, outputDir)


# Wesbarnett, 1fs ts
newSim = SimGromacs([mdp.NPT, dict(mdpFF)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_wb_1fs',
			topol='wb_topol.top',
			coords=currentCoords)
newSim.set_param('nsteps', 4000000) # 4ns
newSim.set_param('dt', 0.001)
newSim.set_param('define', '-DLOPLS')
finalize_simulation(newSim, shellFile, outputDir)



# Minimal, 2fs ts
newSim = SimGromacs([mdp.NPT, dict(mdpFF)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_minimal_2fs',
			topol='minimal_topol.top',
			coords=currentCoords)
newSim.set_param('nsteps', 2000000) # 4ns
newSim.set_param('dt', 0.002)
finalize_simulation(newSim, shellFile, outputDir)


# Minimal, 1fs ts
newSim = SimGromacs([mdp.NPT, dict(mdpFF)], shellFile, 
			mdrun=mdrunCmd,
			suffix='NPT_minimal_1fs',
			topol='minimal_topol.top',
			coords=currentCoords)
newSim.set_param('nsteps', 4000000) # 4ns
newSim.set_param('dt', 0.001)
finalize_simulation(newSim, shellFile, outputDir)



