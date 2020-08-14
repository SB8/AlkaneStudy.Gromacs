#$ -S /bin/bash
#$ -l h_rt=walltime
#$ -l mem=1G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi ncpus
#$ -P Free
#$ -A budgetname
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1
