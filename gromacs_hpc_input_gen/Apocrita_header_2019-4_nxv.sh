#!/bin/bash
#$ -pe smp ncpus
#$ -l h_vmem=1G
#$ -l h_rt=walltime
#$ -l node_type=nxv
#$ -cwd
#$ -N Gromacs
#$ -m b

module load gromacs/2019.4-intelmpi
