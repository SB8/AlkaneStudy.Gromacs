
import os.path
import default_mdp_dicts as mdp

# Define simulation object
class SimGromacs:
	''' Gromacs simulation object used in HPCInputGen (python version) '''

	# Init with list of .mdp parameter dictionaries
	def __init__(self, mdpDicts, fileobj, **kwargs):

		self.mdpDicts = mdpDicts
		self.fileobj = fileobj

		self.grompp = kwargs.get('grompp', 'gmx grompp')
		self.mdrun = kwargs.get('mdrun', 'gmx mdrun')
		self.coords = kwargs.get('coords', 'gro_start.gro')
		self.topol = kwargs.get('topol', 'topol.top')
		self.suffix = kwargs.get('suffix', '')
		self.tableFile = kwargs.get('table', '')
		self.indexFile = kwargs.get('indexFile', '')
		self.coordsOut = "gro_"+self.suffix+".gro"
		self.traj = kwargs.get('traj', 'xtc') # Can pass ['xtc', 'trr'] to use both

		if isinstance(self.traj, str): self.traj = [self.traj]
		self.outputs = ['gro', 'log', 'edr']+self.traj
		
	# Replace or add mdp parameter in highest-level dictionary
	def set_param(self, param, newvalue):
		self.mdpDicts[-1][param] = str(newvalue)

	# Remove parameter
	def remove_param(self, param):
		for d in self.mdpDicts:
			d.pop(param, None)


# Write gromacs commands for sim to fileObj, make corresponding mdp file
def finalize_simulation(sim, shellFile, outputDir):

	# Write .mdp file
	mdpFile = open(os.path.join(outputDir,'mdp_'+sim.suffix+'.mdp'), 'w')
	# Merge dictionaries, overwriting parameters so last dict takes priority
	sortedDict = sim.mdpDicts[0] # Start with first dictionary
	nDicts = len(sim.mdpDicts)
	if nDicts > 1:
		for m in sim.mdpDicts[1:]:
			sortedDict = {**sortedDict, **m}

	# Loop over all mdp parameters, write them if present in dictionary
	# (this ensures params are written in a consistent order)
	for mdpOption in mdp.allMdpOptions:
		if mdpOption in sortedDict:
			mdpFile.write(mdpOption.ljust(24)+'= '+sortedDict[mdpOption]+'\n')

	mdpFile.close()

	gmxFlags = {'gro': 'c', 'log': 'g', 'edr': 'e', 'xtc': 'x', 'trr': 'o'}

	shellFile.write('\n')
	# grompp
	shellFile.write(sim.grompp+' -f mdp_'+sim.suffix+'.mdp -c '+sim.coords)
	shellFile.write(' -p '+sim.topol+' -o tpr_'+sim.suffix+'.tpr')
	if sim.indexFile.strip():
		shellFile.write(' -n '+sim.indexFile)
	shellFile.write('\n')

	# mdrun
	shellFile.write(sim.mdrun+' -s tpr_'+sim.suffix+'.tpr ')
	for op in sim.outputs:
		shellFile.write(' -'+gmxFlags[op]+' '+op+'_'+sim.suffix+'.'+op)
	if sim.tableFile.strip():
		shellFile.write(' -table '+sim.tableFile)
	shellFile.write('\n')



