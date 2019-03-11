
import math
# Tables provide
# f(r), which has r dependence of Coulomb term (should usually be 1/r)
# g(f), for r dependence of attractive/dispersion term (e.g. -1/r^6)
# h(f), for r dependence of repulsive term (e.g. exp(-B*r) or 1/r^12)

# Each line has the format
# r, f, -f', g, -g', h, -h'

# B in repulsive term exp(-B.r)
b = 37.4 # 1/nm
# Exponent of attractive terms
att = 6

step = 0.002 # nm
r_start = 0.04
r_cut = 1.05
r_ext = 1.0

n_switch = int(r_start/step)
n_end = int((r_cut+r_ext)/step) + 1

r_zero = [x*step for x in range(n_switch)]
r_range = [x*step for x in range(n_switch, n_end)]

tfile = open('table_H_H.xvg'.format(b, att), 'w')

# Write r = 0 line (all zeros)
for r in r_zero:
	tfile.write('%15.6e %15.6e %15.6e %15.6e %15.6e %15.6e %15.6e\n' % (r, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))

for r in r_range:
	tfile.write('%15.6e ' % (r,))
	tfile.write('%15.6e %15.6e '  % ( 1/r,     1/r**2))
	tfile.write('%15.6e %15.6e '  % (-1/r**att, -6/r**(att+1)))
	expbr = math.exp(-b*r)
	tfile.write('%15.6e %15.6e\n' % (expbr, b*expbr))
	
