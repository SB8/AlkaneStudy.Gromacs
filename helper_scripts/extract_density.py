import sys, os
import subprocess

# Get index of density in gmx energy menu from command line
rhoNum = sys.argv[1]
print('rhoNum = ', rhoNum)

filelist = os.listdir('.') 
gmxCmd = 'gmx'

for file in filelist:
	# if edr file
	if file[-4:] == '.edr':
		# Create density filename
		rhofile = 'density'+file[3:-4]+'.xvg'

		if not os.path.isfile(rhofile):
			
			edrGet = subprocess.Popen([gmxCmd, 'energy', 
			'-f', file, #'-b', str(bt), '-e', str(et),
			'-o', rhofile], 
			stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
			edr_stdout, edr_err = edrGet.communicate(bytes(str(rhoNum)+'\n', 'utf-8'))
			edrGet.terminate()
