# subprocess module is used to call gromacs commands
import subprocess
import re

startTime = '1000' # picoseconds (as a string)
gmxCmd = 'gmx_d' # Usually 'gmx', but 'gmx_d' for double precision

# Set filenames 
xtcFile = 'xtc_'+suffix+'.xtc'
tprFile = 'tpr_'+suffix+'.tpr'

# Call again to extract properties
shiftStrs = ['0.010', '0.012'] #, '0.014', '0.016', '0.018', '0.020', '0.022', '0.024', '0.026', '0.028', '0.030']

for shift in shiftStrs:
	
	suffix = 'NPT_sim_'+shift
	xtcFile = 'xtc_'+suffix+'.xtc'
	tprFile = 'tpr_'+suffix+'.tpr'
	
	msdGet = subprocess.Popen([gmxCmd, 'msd', '-f', xtcFile, '-s', tprFile, '-b', startTime], stdin = subprocess.PIPE)
	
	msd_stdout, msd_err = msdGet.communicate(b'0\n')
	
	msdText = msd_err.decode('utf-8')
	msdTextArr = msdText.splitlines()

	print(msdTextArr[-2])
	
	# Use regular expression to extract diffucion coeff: D[    System] 2.0968 (+/- 0.0391) 1e-5 cm^2/s
	
	msdGet.terminate()