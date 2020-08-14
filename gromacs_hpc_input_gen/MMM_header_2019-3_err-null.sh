#$ -S /bin/bash
#$ -l h_rt=walltime
#$ -l mem=1G
#$ -l tmpfs=5G
#$ -N GROMACS
#$ -pe mpi ncpus
#$ -P Gold
#$ -A budgetname
#$ -cwd
#$ -e /dev/null

module load gromacs/2019.3/intel-2018

