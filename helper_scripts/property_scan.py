# subprocess module is used to call gromacs commands
import subprocess
import re

startTimeEnergy = '500' # picoseconds (as a string)
startTimeMSD = '500'
gmxCmd = 'gmx' # Usually 'gmx', but 'gmx_d' for double precision


# Call again to extract properties
shiftStrs = ['{:.3f}'.format(i/1000.0) for i in range(0,31,2)]

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

	edr_stdout, edr_err = edrGet.communicate(bytes('14\n18\n', 'utf-8'))
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
	msdRgx = re.match('^D\[\s*System\]\s*(\d*\.?\d+)', msdTextArr[-1])
	#msdRgx = re.match('^<D> =\s*(\d*\.?\d+)\s+.*Error =\s*(\d*\.?\d+)', msdTextArr[-4])

	if msdRgx:
		print(msdRgx.group(1))
	else:
		print("\nNo match for diffusion coefficient in stdout!")

	msdGet.terminate()
