#$ -S /bin/bash
#$ -l h_rt=7:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 48
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NVT_eq_290K.mdp -c gro_240-340K_41150ps.gro -p topol.top -o tpr_NVT_eq_290K.tpr
gerun mdrun_mpi -s tpr_NVT_eq_290K.tpr -c gro_NVT_eq_290K.gro -g log_NVT_eq_290K.log -e edr_NVT_eq_290K.edr -x xtc_NVT_eq_290K.xtc

gmx grompp -f mdp_NPT_eq_290K.mdp -c gro_NVT_eq_290K.gro -p topol.top -o tpr_NPT_eq_290K.tpr
gerun mdrun_mpi -s tpr_NPT_eq_290K.tpr -c gro_NPT_eq_290K.gro -g log_NPT_eq_290K.log -e edr_NPT_eq_290K.edr -x xtc_NPT_eq_290K.xtc -o trr_NPT_eq_290K.trr
