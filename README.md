# AlkaneStudy.Gromacs

## Folder structure


## Force fields and settings

### PYS-W
Paul, W., Yoon, D.Y. and Smith, G.D., 1995. An optimized united atom model for simulations of polymethylene melts. The Journal of chemical physics, 103(4), pp.1702-1709.

```
dt                      = 0.002
cutoff-scheme           = Verlet
coulombtype             = Cut-off ; no charges
rcoulomb                = 1.0
vdwtype                 = Cut-off
rvdw                    = 1.0
```

### TraPPE-UA
```
dt                      = 0.002
cutoff-scheme           = Verlet
coulombtype             = PME
rcoulomb                = 1.4
vdwtype                 = Cut-off
rvdw                    = 1.4
```
### L-OPLS
```
dt                      = 0.002
cutoff-scheme           = Verlet
coulombtype             = PME
rcoulomb                = 1.3
vdwtype                 = Cut-off
vdw-modifier            = Force-switch
rvdw-switch             = 1.1
rvdw                    = 1.3
constraints             = h-bonds
```
### CHARMM
```
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
The 9-6 Lennard-Jones potential must be tabulated, hence vdwtype = User.

With PME electrostatics:

```
dt                      = 0.001
cutoff-scheme           = group
rlist                   = 1.1
coulombtype             = PME
rcoulomb                = 1.0
vdwtype                 = User
vdw-modifier            = Potential-shift
rvdw                    = 1.0
constraints             = h-bonds
```

```

### Flexible-Williams

Williams, D.E., 1967. Nonbonded potential parameters derived from crystalline hydrocarbons. The Journal of Chemical Physics, 47(11), pp.4680-4684.

The original potential was parameterized using a short cutoff (necessary in 1967), but a wide range of cutoffs were used in subsequent MD studies.

No charges are used, so it is less important to use a buffer (buffer = rlist - rvdw).

```
dt                      = 0.001
cutoff-scheme           = group
rlist                   = 1.05
coulombtype             = Cut-off ; no charges
rcoulomb                = 1.0
vdwtype                 = Cut-off
vdw-modifier            = Potential-shift
rvdw                    = 1.0
```
