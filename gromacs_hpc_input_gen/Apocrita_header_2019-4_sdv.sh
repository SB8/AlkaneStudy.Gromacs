#!/bin/bash
#$ -pe parallel ncpus
#$ -l infiniband=sdv-i
#$ -l h_rt=walltime
#$ -cwd
#$ -N Gromacs
#$ -m b

module load gromacs/2019.4-intelmpi
