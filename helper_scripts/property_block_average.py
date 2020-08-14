# subprocess module is used to call gromacs commands
import subprocess
import math
import statistics
import re
import sys

N = 5
nBlocks = 1 # per sim
print('Total number of blocks = ', N*nBlocks)

startTimeMSD = 0
endTimeMSD = 4000
blockStep = round((endTimeMSD - startTimeMSD)/nBlocks)
gmxCmd = 'gmx' # Usually 'gmx', but 'gmx_d' for double precision

rhoNum = sys.argv[1]
print('rhoNum = ', rhoNum)

rhoTot = []
rhoErr = []
diffTot = []
DErr = []

for i in range(0, N):

	tprFile = 'tpr_NPT_sim_'+str(i)+'.tpr'
	edrFile = 'edr_NPT_sim_'+str(i)+'.edr'
	xtcFile = 'xtc_NPT_sim_'+str(i)+'.xtc'
	
	for j in range(0, nBlocks):

		# Define begin time (bt) and end time (et) for block averaging
		bt = startTimeMSD + j*int(blockStep)
		et = bt + int(blockStep)
		print(i, ':', bt, ',', et)

		edrGet = subprocess.Popen([gmxCmd, 'energy', 
			'-f', edrFile, 
			'-b', str(bt),
			'-e', str(et)], 
			stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		edr_stdout, edr_err = edrGet.communicate(bytes(str(rhoNum)+'\n', 'utf-8')) # Set density number
		edrGet.terminate()

		edrTextArr = edr_stdout.decode('utf-8').splitlines()
		
		#densityRgx = re.match('^Density\s+[+-]?((?:[0-9]*\.)?[0-9]+)', edrTextArr[-1])
		# Use string split
		rho_i = edrTextArr[-1].split()[1]
		rhoErr_i = edrTextArr[-1].split()[2]

		print(rho_i, end=',')
		#print(rhoErr_i, end='   -   ')
		rhoTot.append(float(rho_i))
		rhoErr.append(float(rhoErr_i))

		msdGet = subprocess.Popen([gmxCmd, 'msd', 
			'-f', xtcFile, 
			'-s', tprFile, 
			'-b', str(bt),
			'-e', str(et),
			'-o', 'msd_'+str(i)+'-'+str(j)+'.xvg',
			'-mol'], 
			stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		msd_stdout, msd_err = msdGet.communicate(b'0\n')
		msdGet.terminate()

		msdText = msd_stdout.decode('utf-8')
		msdTextArr = msdText.splitlines()
		
		# Use regular expression to extract diffusion coeff <D>
		msdRgx = re.match('^<D> =\s*(\d*\.?\d+)\s+.*Error =\s*(\d*\.?\d+)', msdTextArr[-4])
		#D_i = msdRgx.group(1)
		#DErr_i = msdRgx.group(2)

		# Use string split D[ system]
		D_i = msdTextArr[-1].split()[2]
		DErr_i = msdTextArr[-1].split()[4][0:-1]

		print(D_i)
		#print(DErr_i)
		diffTot.append(float(D_i))
		DErr.append(float(DErr_i))

# Compute overall mean
rho = statistics.mean(rhoTot)
D = statistics.mean(diffTot)

#rhoPlusErr = [abs(rhoTot[i] + rhoErr[i] - rho) for i in range(0,N,1)]
#rhoMinusErr = [abs(rhoTot[i] - rhoErr[i] - rho) for i in range(0,N,1)]

#diffPlusErr = [abs(diffTot[i] + DErr[i] - D) for i in range(0,N,1)]
#diffMinusErr = [abs(diffTot[i] - DErr[i] - D) for i in range(0,N,1)]

# Print overall means
print()
print('{:.5f}'.format(rho), end=',')
print('{:.5f} \n'.format(D))

#print('{:.5f}'.format(max(rhoPlusErr + rhoMinusErr)), end=',') # '+' concatenates lists
#print('{:.5f}'.format(max(diffPlusErr + diffMinusErr)))
#print()

#print('{:.1f}~\\pm~{:.1f}'.format(rho, max(rhoPlusErr + rhoMinusErr)))
#print('{:.3f}~\\pm~{:.3f}'.format(D, max(diffPlusErr + diffMinusErr)))
print('Computing standard error of {} blocks'.format(N*nBlocks))
print('D, stdev, stdev/sqrt(N*nBlocks)')
print('{:.6f}, {:.6f}, {:.6f} \n'.format(D, statistics.stdev(diffTot), statistics.stdev(diffTot)/math.sqrt(N*nBlocks)))
print('rho, stdev, stdev/sqrt(N*nBlocks)')
print('{:.6f}, {:.6f}, {:.6f}'.format(rho, statistics.stdev(rhoTot), statistics.stdev(rhoTot)/math.sqrt(N*nBlocks)))
