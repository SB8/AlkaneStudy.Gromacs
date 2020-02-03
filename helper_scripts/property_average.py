# subprocess module is used to call gromacs commands
import subprocess
import math
import statistics
import re

N = 5
nBlocks = 4
startTimeEnergy = 0 # picoseconds (as a string)
startTimeMSD = 0
endTimeMSD = 4000
blockStep = (endTimeMSD - startTimeMSD)/nBlocks
gmxCmd = 'gmx' # Usually 'gmx', but 'gmx_d' for double precision


rhoTot = []
rhoErr = []
diffTot = []
diffErr = []

for i in range(0, N):

	tprFile = 'tpr_NPT_sim_'+str(i)+'.tpr'
	edrFile = 'edr_NPT_sim_'+str(i)+'.edr'
	xtcFile = 'xtc_NPT_sim_'+str(i)+'.xtc'
	
	for j in range(0, nBlocks):

		# Define begin time (bt) and end time (et) for block averaging
		bt = startTimeMSD + j*int(blockStep)
		et = bt + int(blockStep)
		print(bt, end=',')
		print(et)

		edrGet = subprocess.Popen([gmxCmd, 'energy', 
			'-f', edrFile, 
			'-b', str(bt),
			'-e', str(et)], 
			stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		edr_stdout, edr_err = edrGet.communicate(bytes('21\n', 'utf-8')) # Set density number
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
			'-mol'], 
			stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		
		msd_stdout, msd_err = msdGet.communicate(b'0\n')
		msdGet.terminate()

		msdText = msd_stdout.decode('utf-8')
		msdTextArr = msdText.splitlines()
		
		# Use regular expression to extract diffucion coeff
		#msdRgx = re.match('^<D> =\s*(\d*\.?\d+)\s+.*Error =\s*(\d*\.?\d+)', msdTextArr[-4])
		# Use string split
		D_i = msdTextArr[-1].split()[2]
		diffErr_i = msdTextArr[-1].split()[4][0:-1]

		print(D_i)
		#print(diffErr_i)
		diffTot.append(float(D_i))
		diffErr.append(float(diffErr_i))

	#if msdRgx:
	#	print(msdRgx.group(1))
		#diffTot.append(float(msdRgx.group(1)))
	#else:
	#	print("\nNo match for diffusion coefficient in stdout!")

rho = statistics.mean(rhoTot)
D = statistics.mean(diffTot)

rhoPlusErr = [abs(rhoTot[i] + rhoErr[i] - rho) for i in range(0,N,1)]
rhoMinusErr = [abs(rhoTot[i] - rhoErr[i] - rho) for i in range(0,N,1)]

diffPlusErr = [abs(diffTot[i] + diffErr[i] - D) for i in range(0,N,1)]
diffMinusErr = [abs(diffTot[i] - diffErr[i] - D) for i in range(0,N,1)]

print()
print('{:.5f}'.format(rho), end=',')
print('{:.5f}'.format(D))

#print('{:.5f}'.format(max(rhoPlusErr + rhoMinusErr)), end=',') # '+' concatenates lists
#print('{:.5f}'.format(max(diffPlusErr + diffMinusErr)))
#print()

#print('{:.1f}~\\pm~{:.1f}'.format(rho, max(rhoPlusErr + rhoMinusErr)))
#print('{:.3f}~\\pm~{:.3f}'.format(D, max(diffPlusErr + diffMinusErr)))
print('Computing standard error of {} blocks'.format(N*nBlocks))
print('{:.3f}  {:.5f}'.format(statistics.stdev(diffTot), statistics.stdev(diffTot)/math.sqrt(N*nBlocks)))