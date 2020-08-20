# AlkaneStudy.Gromacs

## Folder structure


## Force field .mdp settings

### PYS-W
Paul, W., Yoon, D. Y. and Smith, G. D. (1995) ‘An optimized united atom model for simulations of polymethylene melts’, The Journal of Chemical Physics, 103(4), pp. 1702–1709. doi: 10.1063/1.469740.

```
dt                      = 0.002
cutoff-scheme           = Verlet
coulombtype             = Cut-off ; no charges
rcoulomb                = 1.0
vdwtype                 = Cut-off
rvdw                    = 1.0
DispCorr                = EnerPres
```

### TraPPE-UA
Martin, M. G. and Siepmann, J. I. (1998) ‘Transferable potentials for phase equilibria. 1. United-atom description of n-alkanes’, Journal of Physical Chemistry B, 102(14), pp. 2569–2577. doi: 10.1021/jp972543+.

```
dt                      = 0.002
cutoff-scheme           = Verlet
coulombtype             = PME ; Cut-off if no charges present
rcoulomb                = 1.4
vdwtype                 = Cut-off
rvdw                    = 1.4
DispCorr                = EnerPres
constraints             = all-bonds
```
### L-OPLS
Siu, S. W. I., Pluhackova, K. and Böckmann, R. A. (2012) ‘Optimization of the OPLS-AA force field for long hydrocarbons’, Journal of Chemical Theory and Computation, 8(4), pp. 1459–1470. doi: 10.1021/ct200908r.

```
dt                      = 0.002
cutoff-scheme           = Verlet
coulombtype             = PME
rcoulomb                = 1.3
vdwtype                 = Cut-off
vdw-modifier            = Force-switch
rvdw-switch             = 1.1
rvdw                    = 1.3
DispCorr                = EnerPres
constraints             = h-bonds
```
### CHARMM
Klauda, J. B. et al. (2010) ‘Update of the CHARMM All-Atom Additive Force Field for Lipids: Validation on Six Lipid Types’, Journal of Physical Chemistry B, 114(23), pp. 7830–7843. doi: 10.1021/jp101759q.

```
dt                      = 0.001
cutoff-scheme           = Verlet
coulombtype             = PME
rcoulomb                = 1.2
vdwtype                 = Cut-off
vdw-modifier            = Force-switch
rvdw-switch             = 1.0
rvdw                    = 1.2
constraints             = h-bonds
```

### COMPASS-gmx
Sun, H. (1998) ‘Compass: An ab initio force-field optimized for condensed-phase applications - Overview with details on alkane and benzene compounds’, Journal of Physical Chemistry B, pp. 7338–7364. doi: 10.1021/jp980939v.

The 9-6 Lennard-Jones potential must be tabulated, hence vdwtype = User.

```
dt                      = 0.001
cutoff-scheme           = group
rlist                   = 1.1
coulombtype             = PME
rcoulomb                = 1.0
vdwtype                 = User
vdw-modifier            = Potential-shift
rvdw                    = 1.0
DispCorr                = EnerPres
constraints             = h-bonds
```

### Williams 7B

Pair potential: Williams, D. E. (1967) ‘Nonbonded potential parameters derived from crystalline hydrocarbons’, The Journal of Chemical Physics, 47(11), pp. 4680–4684. doi: 10.1063/1.1701684.

Torsion potential: Tu, K., Tobias, D. J. and Klein, M. L. (1995), Journal of Physical Chemistry, 99(24), pp. 10035–10042. doi: 10.1021/j100024a053.

```
dt                      = 0.001
cutoff-scheme           = group ; if using tabulated potential
rlist                   = 1.05
coulombtype             = Cut-off ; no charges
rcoulomb                = 1.0
vdwtype                 = Cut-off
vdw-modifier            = Potential-shift
rvdw                    = 1.0
DispCorr                = EnerPres
constraints             = h-bonds
```

## Ensemble .mdp settings