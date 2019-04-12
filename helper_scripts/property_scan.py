# subprocess module is used to call gromacs commands
import subprocess
import re

boxSelect = 15
densitySelect = 19
startTimeEnergy = '1000' # picoseconds (as a string)
startTimeMSD = '1000'
gmxCmd = 'gmx_d' # Usually 'gmx', but 'gmx_d' for double precision


# Call again to extract properties
shiftStrs = ['0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022', '0.024', '0.026', '0.028', '0.030']

for shift in shiftStrs:
	
	suffix = 'NPT_sim_'+shift

	tprFile = 'tpr_'+suffix+'.tpr'
	edrFile = 'edr_'+suffix+'.edr'
	xtcFile = 'xtc_'+suffix+'.xtc'
	
	# Get average box dimensions and density
	edrGet = subprocess.Popen([gmxCmd, 'energy', 
		'-f', edrFile, 
		'-b', startTimeEnergy], 
		stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	edr_stdout, edr_err = edrGet.communicate(bytes('15\n19\n', 'utf-8'))
	edrGet.terminate()
	
	edrTextArr = edr_stdout.decode('utf-8').splitlines()

	boxRgx = re.match('^\s*Box\-X\s+[+-]?((?:[0-9]*\.)?[0-9]+)', edrTextArr[-2])
	densityRgx = re.match('\s*^Density\s+[+-]?((?:[0-9]*\.)?[0-9]+)', edrTextArr[-1])

	print(boxRgx.group(1), end = ',')
	print(densityRgx.group(1), end = ',')
	
	# Get diffusion coefficient
	msdGet = subprocess.Popen([gmxCmd, 'msd', 
		'-f', xtcFile, 
		'-s', tprFile, 
		'-b', startTimeMSD,
		'-mol'], 
		stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	msd_stdout, msd_err = msdGet.communicate(b'0\n')
	
	msdText = msd_stdout.decode('utf-8')
	msdTextArr = msdText.splitlines()

	# Use regular expression to extract diffucion coeff
	#msdRgx = re.match('^D\[    System\]\s*(\d*\.?\d+)', msdTextArr[-1])
	msdRgx = re.match('^<D> =\s*(\d*\.?\d+)\s+.*Error =\s*(\d*\.?\d+)', msdTextArr[-4])

	if msdRgx:
		print(msdRgx.group(1))
	else:
		print("\nNo match for diffusion coefficient in stdout!")

	msdGet.terminate()
