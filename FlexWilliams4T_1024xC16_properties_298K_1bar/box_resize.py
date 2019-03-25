
import sys, subprocess

# Need to know: grofile to read, gmx editconf command, scaling factor, grofile to output
gmx = sys.argv[1]
groFile = sys.argv[2]
scaleFac = sys.argv[3]
outFile = sys.argv[4]

with open(groFile, 'r') as f:
    lines = f.read().splitlines()
    boxline = lines[-1].strip()

# Parse box-z as number
boxvectors = boxline.split()
lx = boxvectors[0]
ly = boxvectors[1]
lz = str(float(scaleFac)*float(boxvectors[2]))

# Call editconf
subprocess.run([gmx, 'editconf', '-f', groFile, '-pbc', '-box', lx, ly, lz, '-o', outFile])