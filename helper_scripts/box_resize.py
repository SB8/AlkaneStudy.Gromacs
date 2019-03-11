
import sys

# Need to know: grofile to read, gmx editconf command, scaling factor, grofile to output
gmx = sys.argv[0]
groFile = sys.argv[1]
scaleFac = sys.argv[2]
outFile = sys.argv[3]

with open(groFile, 'r') as f:
    lines = f.read().splitlines()
    boxline = lines[-1]

# Split string

# Parse box-z as number
boxvectors = boxline.split()
lx = boxvectors[0]+' '
ly = boxvectors[1]+' '
lz = str(scaleFac*float(boxvectors[2]))

# Call editconf
editconf = gmx+' editconf -f '+groFile+' -box '+lx+ly+lz+' -o '+outFile
print(editconf)

# subprocess.run([gmx, 'editconf', '-f', groFile, 
#   '-box', lx, ly, lz,
#   '-o', outFile])