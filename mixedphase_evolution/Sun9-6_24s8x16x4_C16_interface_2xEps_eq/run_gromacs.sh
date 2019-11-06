#$ -S /bin/bash
#$ -l h_rt=23:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 96
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd
#$ -e /dev/null

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NP6T_313K.mdp -c gro_NP3T_2xEps_313K.gro -p topol.top -o tpr_NP6T_313K.tpr
gerun mdrun_mpi -s tpr_NP6T_313K.tpr -c gro_NP6T_313K.gro -g log_NP6T_313K.log -e edr_NP6T_313K.edr -x xtc_NP6T_313K.xtc -table table6-9.xvg
