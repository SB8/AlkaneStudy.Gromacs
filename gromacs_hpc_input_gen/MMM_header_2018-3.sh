#$ -S /bin/bash
#$ -l h_rt=walltime
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi ncpus
#$ -P Gold
#$ -A budgetname
#$ -cwd

module load gromacs/2018.3/intel-2018

