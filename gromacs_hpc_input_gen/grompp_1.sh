#!/bin/sh
#$ -cwd
#$ -pe smp 4
#$ -l h_vmem=1G
#$ -l node_type=nxv
#$ -l h_rt=1:0:0

module load gromacs/2019.4-intelmpi

