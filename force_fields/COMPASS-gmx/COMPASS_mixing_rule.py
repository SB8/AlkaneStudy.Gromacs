
import math

# C, H
atomnames = ['C_4', 'H_1']
eps = [0.259408, 0.096232]
r0 = [0.38540, 0.28780]

numatoms = len(eps)

for i in range(numatoms):
    for j in range(i, numatoms):
        
        ri3 = r0[i]**3
        rj3 = r0[j]**3
        ri6 = r0[i]**6
        rj6 = r0[j]**6

        eps_ij = 2.0*math.sqrt(eps[i]*eps[j])*(ri3*rj3)/(ri6 + rj6)
        r0_ij = ((ri6 + rj6)/2.0)**(1.0/6.0)
        
        print('%f %f\n' % (eps_ij, r0_ij))
        print('%s %s %10.4e %10.4e\n' % (atomnames[i], atomnames[j], 3.0*eps_ij*(r0_ij**6), 2.0*eps_ij*(r0_ij**9)))


