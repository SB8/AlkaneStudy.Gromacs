
# Settings related to the force field or output only
# no dt, ref-t or ref-p because meaningless for EM
TraPPE = {
	'integrator': 'md',
	'dt': '0.002',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '1000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'Verlet',
	'coulombtype': 'PME',
	'rcoulomb': '1.4',
	'vdwtype': 'Cut-off',
	'rvdw': '1.4',
	'DispCorr': 'EnerPres',
	
	'constraints': 'all-bonds',
	'constraint-algorithm': 'Lincs',
	'lincs-order': '4',
	'lincs-iter': '1'}

PYSW = {
	'integrator': 'md',
	'dt': '0.002',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '1000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'Verlet',
	'coulombtype': 'Cut-off',
	'rcoulomb': '1.2', 
	'vdwtype': 'Cut-off',
	# Waheed uses 1.2 nm, PYS and PengYi use 1.0
	'rvdw': '1.2',
	'DispCorr': 'EnerPres',
	
	'constraints': 'none'}

L_OPLS = {
	'integrator': 'md',
	'dt': '0.002',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '2000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'Verlet',
	'coulombtype': 'PME',
	'rcoulomb': '1.3',
	'vdwtype': 'Cut-off',
	'vdw-modifier': 'Force-switch',
	'rvdw': '1.3',
	'rvdw-switch': '1.1',
	'DispCorr': 'EnerPres',
	
	'constraints': 'h-bonds',
	'constraint-algorithm': 'Lincs',
	'lincs-order': '4',
	'lincs-iter': '1'}

CHARMM36 = {
	'integrator': 'md',
	'dt': '0.001',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '2000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'Verlet',
	'rlist': '1.2', # Will be automatically set in Verlet scheme anyway
	'coulombtype': 'PME',
	'rcoulomb': '1.2',
	'vdwtype': 'Cut-off',
	'vdw-modifier': 'Force-switch',
	'rvdw': '1.2',
	'rvdw-switch': '1.0',
	'DispCorr': 'EnerPres',
	
	'constraints': 'h-bonds',
	'constraint-algorithm': 'Lincs',
	'lincs-order': '4',
	'lincs-iter': '1'}

FlexWilliams = {
	'integrator': 'md',
	'dt': '0.001',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '2000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'group',
	'rlist': '1.05', # Small buffer
	'coulombtype': 'Cut-off',
	'rcoulomb': '1.05',
	'vdwtype': 'Cut-off', # Tabulated (vdwtype=User) can be faster
	'vdw-modifier': 'Potential-shift',
	'rvdw': '1.0',
	'DispCorr': 'EnerPres',
	
	'constraints': 'none'}

FlexWilliamsLincs = {
	'integrator': 'md',
	'dt': '0.001',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '2000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'group',
	'rlist': '1.05', # Small buffer
	'coulombtype': 'Cut-off',
	'rcoulomb': '1.05',
	'vdwtype': 'Cut-off', # Tabulated (vdwtype=User) can be faster
	'vdw-modifier': 'Potential-shift',
	'rvdw': '1.0',
	'DispCorr': 'EnerPres',
	
	'constraints': 'h-bonds',
	'constraint-algorithm': 'Lincs',
	'lincs-order': '4',
	'lincs-iter': '1'}

COMPASS = {
	'integrator': 'md',
	'dt': '0.001',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '2000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'group',
	# Small buffer - no charge groups should be used (each atom should be its own charge group)
	'rlist': '1.1',
	'coulombtype': 'PME',
	'rcoulomb': '1.1',
	'vdwtype': 'User',
	'vdw-modifier': 'Potential-shift',
	'rvdw': '1.0',
	'DispCorr': 'EnerPres',
	
	'constraints': 'none'}

COMPASS_LINCS = {
	'integrator': 'md',
	'dt': '0.001',
	'nstlog': '1000',
	'nstcalcenergy': '100',
	'nstenergy': '1000',
	'nstxout-compressed': '2000',
	'compressed-x-precision': '1000',
	
	'cutoff-scheme': 'group',
	# Small buffer - no charge groups should be used (each atom should be its own charge group)
	'rlist': '1.1',
	'coulombtype': 'PME',
	'rcoulomb': '1.1',
	'vdwtype': 'User',
	'vdw-modifier': 'Potential-shift',
	'rvdw': '1.0',
	'DispCorr': 'EnerPres',
	
	'constraints': 'h-bonds',
    'constraint-algorithm': 'Lincs'}


# Steepest descent EM
EM = {
	'integrator': 'steep',
	'nsteps': '10000',
	'emtol': '100.0',
	'nstxout': '100',
	'constraints': 'none'}

# Generic NPT sim
NPT = {
	'ref-t': '298',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'ref-p': '1.0',
	'Pcoupl': 'Parrinello-Rahman',
	'tau-p': '2.0',
	'compressibility': '5e-5'}

# NPT with berendsen thermostat (1ps time constant)
NPT_eq = {
	'ref-t': '298',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'ref-p': '1.0',
	'Pcoupl': 'Berendsen',
	'tau-p': '1.0',
	'compressibility': '5e-5',
	'gen-vel': 'yes',
	'gen-temp': '298', # Could add warning if this is different to ref-t
	'gen-seed': '-1'}

# Generic NVT sim
NVT = {
	'ref-t': '298',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'Pcoupl': 'no'}

# For simulations of interfaces with incraesed r_vdw (5*sigma_CH₂) and semiisotropic Pcoupl
NPzT_interface = {
	'ref-t': '298',
	'rcoulomb': '1.875',
	'rvdw': '1.875',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'Pcoupl': 'Parrinello-Rahman',
	'Pcoupltype': 'semiisotropic',
	'tau-p': '2.0',
	'compressibility': '0.0 5e-5', # x-y and z
	'ref-p': '1.0 1.0'}

# For simulations of interfaces with incraesed r_vdw (5*σ_CH₂) and surface tension coupling 
# Default γ = 10 mN/m, so γ*2 = 200 bar nm
NPγT_interface = {
	'ref-t': '298',
	'rcoulomb': '1.875',
	'rvdw': '1.875',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'Pcoupl': 'Parrinello-Rahman',
	'Pcoupltype': 'surface-tension',
	'tau-p': '2.0',
	'compressibility': '5e-5 5e-5', # x-y and z
	'ref-p': '200.0 1.0'}

# For NPT simulations of interfaces with PME treatment of VdW - no DispCorr
# Constant interface area (in x-y plane)
# Useful for liquid-vapour systems
NPT_interface_PMEVdW = {
	'ref-t': '298',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'ref-p': '1.0',
	'Pcoupl': 'Parrinello-Rahman',
	'Pcoupltype': 'semiisotropic',
	'tau-p': '2.0',
	'compressibility': '0.0 5e-5', # x-y and z
	'ref-p': '1.0 1.0',
	'vdwtype': 'PME',
	'lj-pme-comb-rule': 'Geometric',
	'DispCorr': 'no'}

# For NVT simulations of interfaces with PME treatment of VdW - no DispCorr
# Useful for liquid-vapour systems where accurate pressure measurements are needed
NVT_interface_PMEVdW = {
	'ref-t': '298',
	'tcoupl': 'v-rescale',
	'tc-grps': 'System',
	'tau-t': '0.1',
	'Pcoupl': 'no',
	'vdwtype': 'PME',
	'lj-pme-comb-rule': 'Geometric',
	'DispCorr': 'no'}

allMdpOptions = [
'include',
'define',
'integrator',
'tinit',
'dt',
'nsteps',
'init-step',
'simulation-part',
'comm-mode',
'nstcomm',
'comm-grps',
'bd-fric',
'ld-seed',
'emtol',
'emstep',
'niter',
'fcstep',
'nstcgsteep',
'nbfgscorr',
'rtpi',
'nstxout',
'nstvout',
'nstfout',
'nstlog',
'nstcalcenergy',
'nstenergy',
'nstxout-compressed',
'compressed-x-precision',
'compressed-x-grps',
'energygrps',
'cutoff-scheme',
'nstlist',
'ns-type',
'pbc',
'periodic-molecules',
'verlet-buffer-tolerance',
'rlist',
'coulombtype',
'coulomb-modifier',
'rcoulomb-switch',
'rcoulomb',
'epsilon-r',
'epsilon-rf',
'vdwtype',
'vdw-modifier',
'rvdw-switch',
'rvdw',
'DispCorr',
'table-extension',
'energygrp-table',
'fourierspacing',
'fourier-nx',
'fourier-ny',
'fourier-nz',
'pme-order',
'ewald-rtol',
'ewald-rtol-lj',
'lj-pme-comb-rule',
'ewald-geometry',
'epsilon-surface',
'implicit-solvent',
'gb-algorithm',
'nstgbradii',
'rgbradii',
'gb-epsilon-solvent',
'gb-saltconc',
'gb-obc-alpha',
'gb-obc-beta',
'gb-obc-gamma',
'gb-dielectric-offset',
'sa-algorithm',
'sa-surface-tension',
'tcoupl',
'nsttcouple',
'nh-chain-length',
'print-nose-hoover-chain-variables',
'tc-grps',
'tau-t',
'ref-t',
'Pcoupl',
'Pcoupltype',
'nstPcouple',
'tau-p',
'compressibility',
'ref-p',
'refcoord_scaling',
'QMMM',
'QMMM-grps',
'QMmethod',
'QMMMscheme',
'QMbasis',
'QMcharge',
'QMmult',
'SH',
'CASorbitals',
'CASelectrons',
'SAon',
'SAoff',
'SAsteps',
'MMChargeScaleFactor',
'bOPT',
'bTS',
'annealing',
'annealing-npoints',
'annealing-time',
'annealing-temp',
'gen-vel',
'gen-temp',
'gen-seed',
'constraints',
'constraint-algorithm',
'continuation',
'Shake-SOR',
'shake-tol',
'lincs-order',
'lincs-iter',
'lincs-warnangle',
'morse',
'energygrp-excl',
'nwall',
'wall-type',
'wall-r-linpot',
'wall-atomtype',
'wall-density',
'wall-ewald-zfac',
'pull',
'rotation',
'IMD-group',
'disre',
'disre-weighting',
'disre-mixed',
'disre-fc',
'disre-tau',
'nstdisreout',
'orire',
'orire-fc',
'orire-tau',
'orire-fitgrp',
'nstorireout',
'free-energy',
'couple-moltype',
'couple-lambda0',
'couple-lambda1',
'couple-intramol',
'init-lambda',
'init-lambda-state',
'delta-lambda',
'nstdhdl',
'fep-lambdas',
'mass-lambdas',
'coul-lambdas',
'vdw-lambdas',
'bonded-lambdas',
'restraint-lambdas',
'temperature-lambdas',
'calc-lambda-neighbors',
'init-lambda-weights',
'dhdl-print-energy',
'sc-alpha',
'sc-power',
'sc-r-power',
'sc-sigma',
'sc-coul',
'separate-dhdl-file',
'dhdl-derivatives',
'dh_hist_size',
'dh_hist_spacing',
'acc-grps',
'accelerate',
'freezegrps',
'freezedim',
'cos-acceleration',
'deform',
'simulated-tempering',
'simulated-tempering-scaling',
'sim-temp-low',
'sim-temp-high',
'E-x',
'E-xt',
'E-y',
'E-yt',
'E-z',
'E-zt',
'swapcoords',
'adress',
'user1-grps',
'user2-grps',
'userint1',
'userint2',
'userint3',
'userint4',
'userreal1',
'userreal2',
'userreal3',
'userreal4']
