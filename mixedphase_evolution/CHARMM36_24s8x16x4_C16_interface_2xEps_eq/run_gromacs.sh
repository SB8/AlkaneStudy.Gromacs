#$ -S /bin/bash
#$ -l h_rt=23:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 72
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

gmx grompp -f mdp_EM_2xEps_360K.mdp -c C16_24x16x4_solid8_add2x0x0.gro -p topol_2xEps.top -o tpr_EM_2xEps_360K.tpr
gerun mdrun_mpi -s tpr_EM_2xEps_360K.tpr -c gro_EM_2xEps_360K.gro -g log_EM_2xEps_360K.log -e edr_EM_2xEps_360K.edr -x xtc_EM_2xEps_360K.xtc

gmx grompp -f mdp_NVTeq_2xEps_360K.mdp -c gro_EM_2xEps_360K.gro -p topol_2xEps.top -o tpr_NVTeq_2xEps_360K.tpr
gerun mdrun_mpi -s tpr_NVTeq_2xEps_360K.tpr -c gro_NVTeq_2xEps_360K.gro -g log_NVTeq_2xEps_360K.log -e edr_NVTeq_2xEps_360K.edr -x xtc_NVTeq_2xEps_360K.xtc

gmx grompp -f mdp_NP3T_2xEps_304K.mdp -c gro_NVTeq_2xEps_360K.gro -p topol_2xEps.top -o tpr_NP3T_2xEps_304K.tpr
gerun mdrun_mpi -s tpr_NP3T_2xEps_304K.tpr -c gro_NP3T_2xEps_304K.gro -g log_NP3T_2xEps_304K.log -e edr_NP3T_2xEps_304K.edr -x xtc_NP3T_2xEps_304K.xtc

gmx grompp -f mdp_NP6T_304K.mdp -c gro_NP3T_2xEps_304K.gro -p topol.top -o tpr_NP6T_304K.tpr
gerun mdrun_mpi -s tpr_NP6T_304K.tpr -c gro_NP6T_304K.gro -g log_NP6T_304K.log -e edr_NP6T_304K.edr -x xtc_NP6T_304K.xtc
