#$ -S /bin/bash
#$ -l h_rt=23:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 96
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_EM.mdp -c C15_15x10x3_Pbcm.gro -p topol.top -o tpr_EM.tpr
gerun mdrun_mpi -s tpr_EM.tpr -c gro_EM.gro -g log_EM.log -e edr_EM.edr -o trr_EM.trr

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq.tpr
gerun mdrun_mpi -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc

gmx grompp -f mdp_NPT_tau-p_3.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_tau-p_3.tpr
gerun mdrun_mpi -s tpr_NPT_tau-p_3.tpr -c gro_NPT_tau-p_3.gro -g log_NPT_tau-p_3.log -e edr_NPT_tau-p_3.edr -x xtc_NPT_tau-p_3.xtc

gmx grompp -f mdp_NPT_tau-p_4.mdp -c gro_NPT_tau-p_3.gro -p topol.top -o tpr_NPT_tau-p_4.tpr
gerun mdrun_mpi -s tpr_NPT_tau-p_4.tpr -c gro_NPT_tau-p_4.gro -g log_NPT_tau-p_4.log -e edr_NPT_tau-p_4.edr -x xtc_NPT_tau-p_4.xtc

gmx grompp -f mdp_NPT_tau-p_5.mdp -c gro_NPT_tau-p_4.gro -p topol.top -o tpr_NPT_tau-p_5.tpr
gerun mdrun_mpi -s tpr_NPT_tau-p_5.tpr -c gro_NPT_tau-p_5.gro -g log_NPT_tau-p_5.log -e edr_NPT_tau-p_5.edr -x xtc_NPT_tau-p_5.xtc

gmx grompp -f mdp_NPT_tau-p_6.mdp -c gro_NPT_tau-p_5.gro -p topol.top -o tpr_NPT_tau-p_6.tpr
gerun mdrun_mpi -s tpr_NPT_tau-p_6.tpr -c gro_NPT_tau-p_6.gro -g log_NPT_tau-p_6.log -e edr_NPT_tau-p_6.edr -x xtc_NPT_tau-p_6.xtc

gmx grompp -f mdp_NPT_tau-p_8.mdp -c gro_NPT_tau-p_6.gro -p topol.top -o tpr_NPT_tau-p_8.tpr
gerun mdrun_mpi -s tpr_NPT_tau-p_8.tpr -c gro_NPT_tau-p_8.gro -g log_NPT_tau-p_8.log -e edr_NPT_tau-p_8.edr -x xtc_NPT_tau-p_8.xtc

gmx grompp -f mdp_NPT_tau-p_10.mdp -c gro_NPT_tau-p_8.gro -p topol.top -o tpr_NPT_tau-p_10.tpr
gerun mdrun_mpi -s tpr_NPT_tau-p_10.tpr -c gro_NPT_tau-p_10.gro -g log_NPT_tau-p_10.log -e edr_NPT_tau-p_10.edr -x xtc_NPT_tau-p_10.xtc
