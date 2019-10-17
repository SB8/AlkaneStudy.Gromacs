# subprocess module is used to call gromacs commands
import subprocess
import statistics
import re


iter = 0
Trange = [284, 290, 296, 302, 308, 314]

gmxCmd = 'gmx' # Usually 'gmx', but 'gmx_d' for double precision

for T in Trange:

	edrFile = 'edr_NPT_'+str(T)+'K_'+str(iter)+'.edr'
	xvgFile = 'density_NPT_'+str(T)+'K_'+str(iter)+'.xvg'
	
	edrGet = subprocess.Popen([gmxCmd, 'energy', 
		'-f', edrFile, 
		'-o', xvgFile], 
		stdin = subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	edr_stdout, edr_err = edrGet.communicate(bytes('17\n', 'utf-8'))
	edrGet.terminate()
	
