# subprocess module is used to call gromacs commands
import subprocess
import re

startTime = '3000' # picoseconds (as a string)
gmxCmd = 'gmx' # Usually 'gmx', but 'gmx_d' for double precision


# Call again to extract properties
shiftStrs = ['0.010', '0.012', '0.014', '0.016', '0.018', '0.020', '0.022', '0.024', '0.026', '0.028', '0.030']

for shift in shiftStrs:
	
	suffix = 'NPT_sim_'+shift
	xtcFile = 'xtc_'+suffix+'.xtc'
	tprFile = 'tpr_'+suffix+'.tpr'
	
	msdGet = subprocess.Popen([gmxCmd, 'msd', 
		'-f', xtcFile, 
		'-s', tprFile, 
		'-b', startTime,
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
		print("No match for diffusion coefficient in stdout!")

	msdGet.terminate()
