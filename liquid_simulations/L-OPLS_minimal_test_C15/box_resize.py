
import sys, subprocess

# Need to know: grofile to read, gmx editconf command, scaling factor, grofile to output
gmx = sys.argv[1]
suffix = sys.argv[2]
scaleFac = sys.argv[3]
outFile = sys.argv[4]

groFile = 'gro_'+suffix+'.gro'
tprFile = 'tpr_'+suffix+'.tpr'

with open(groFile, 'r') as f:
    lines = f.read().splitlines()
    boxline = lines[-1].strip()

# Parse box-z as number
boxvectors = boxline.split()
lx = boxvectors[0]
ly = boxvectors[1]
lz = str(float(scaleFac)*float(boxvectors[2]))

# Call trjconv to remove pbcs (make molecules whole again)
trjconv = subprocess.Popen([gmx, 'trjconv', '-f', groFile, '-s', tprFile, '-pbc', 'mol', '-o', 'gro_temp.gro'], stdin=subprocess.PIPE)
trjconv_stdout, trjconv_err = trjconv.communicate(b'0\n')
trjconv.terminate()

# Call trjconv to enlarge box in z direction
trjconv2 = subprocess.Popen([gmx, 'trjconv', '-f', 'gro_temp.gro', '-s', tprFile, '-box', lx, ly, lz, '-center', '-o', 'gro_interface_start.gro'], stdin=subprocess.PIPE)
trjconv2_stdout, trjconv2_err = trjconv2.communicate(b'0\n0\n')
trjconv2.terminate()
