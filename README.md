# AlkaneStudy.Gromacs

## Folder structure


## Force field .mdp settings

### PYS-W
W. Paul, D. Y. Yoon, and G. D. Smith, J. Chem. Phys. 103, 1702 (1995)

https://doi.org/10.1063/1.469740

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
M.G. Martin and J.I. Siepmann, J. Phys. Chem. B, Vol. 102, No. 14, 1998

https://doi.org/10.1021/jp972543+
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
S.W.I. Siu, K. Pluhackova, and R.A. Böckmann, J. Chem. Theory Comput. 2012, 8, 4, 1459–1470

https://doi.org/10.1021/ct200908r
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
J.B. Klauda, R.M. Venable, J.A. Freites, J.W. O’Connor, D.J. Tobias, C. Mondragon-Ramirez, I. Vorobyov, A.D. MacKerell Jr., J. Phys. Chem. B 2010, 114, 7830–7843

https://doi.org/10.1021/jp101759q
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
H. Sun, J. Phys. Chem. B 1998, 102, 7338-7364

https://doi.org/10.1021/jp980939v

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

Pair potential: D.E. Williams, J. Chem. Phys. 47, 4680 (1967)

https://doi.org/10.1063/1.1701684

Torsion potential: K. Tu, D.J. Tobias, and M.L. Klein, J. Phys. Chem. 1995, 99, 24, 10035–10042

https://doi.org/10.1021/j100024a053

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