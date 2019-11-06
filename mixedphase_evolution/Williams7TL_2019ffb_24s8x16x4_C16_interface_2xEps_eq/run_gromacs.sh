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

gmx grompp -f mdp_NP3T_2xEps_306K.mdp -c gro_NVTeq_2xEps_360K.gro -p topol.top -o tpr_NP3T_2xEps_306K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NP3T_2xEps_306K.tpr -c gro_NP3T_2xEps_306K.gro -g log_NP3T_2xEps_306K.log -e edr_NP3T_2xEps_306K.edr -x xtc_NP3T_2xEps_306K.xtc -table table.xvg

gmx grompp -f mdp_NP6T_306K.mdp -c gro_NP3T_2xEps_306K.gro -p topol.top -o tpr_NP6T_306K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NP6T_306K.tpr -c gro_NP6T_306K.gro -g log_NP6T_306K.log -e edr_NP6T_306K.edr -x xtc_NP6T_306K.xtc -table table.xvg
