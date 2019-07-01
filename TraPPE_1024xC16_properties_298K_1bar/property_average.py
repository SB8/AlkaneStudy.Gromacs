# subprocess module is used to call gromacs commands
import subprocess
import statistics
import re

startTimeEnergy = '500' # picoseconds (as a string)
startTimeMSD = '500'
gmxCmd = 'gmx' # Usually 'gmx', but 'gmx_d' for double precision

N = 3
densityTot = []
diffTot = []

for i in range(0,N,1):

	tprFile = 'tpr_NPT_sim_'+str(i)+'.tpr'
	edrFile = 'edr_NPT_sim_'+str(i)+'.edr'
	xtcFile = 'xtc_NPT_sim_'+str(i)+'.xtc'
	
	edrGet = subprocess.Popen([gmxCmd, 'energy', 
		'-f', edrFile, 
		'-b', startTimeEnergy], 
		stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	edr_stdout, edr_err = edrGet.communicate(bytes('17\n', 'utf-8'))
	edrGet.terminate()

	edrTextArr = edr_stdout.decode('utf-8').splitlines()
	
	densityRgx = re.match('^Density\s+[+-]?((?:[0-9]*\.)?[0-9]+)', edrTextArr[-1])
	print(densityRgx.group(1), end=',')
	densityTot.append(float(densityRgx.group(1)))
	
	msdGet = subprocess.Popen([gmxCmd, 'msd', 
		'-f', xtcFile, 
		'-s', tprFile, 
		'-b', startTimeMSD,
		'-mol'], 
		stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	msd_stdout, msd_err = msdGet.communicate(b'0\n')
	msdGet.terminate()

	msdText = msd_stdout.decode('utf-8')
	msdTextArr = msdText.splitlines()
	
	# Use regular expression to extract diffucion coeff
	msdRgx = re.match('^<D> =\s*(\d*\.?\d+)\s+.*Error =\s*(\d*\.?\d+)', msdTextArr[-4])
	
	if msdRgx:
		print(msdRgx.group(1))
		diffTot.append(float(msdRgx.group(1)))
	else:
		print("\nNo match for diffusion coefficient in stdout!")
		
	
print(statistics.mean(densityTot), end=',')
print(statistics.mean(diffTot))
