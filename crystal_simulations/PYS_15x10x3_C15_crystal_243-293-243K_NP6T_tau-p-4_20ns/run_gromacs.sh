#$ -S /bin/bash
#$ -l h_rt=48:00:00
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

gmx grompp -f mdp_NP3T_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NP3T_eq.tpr
gerun mdrun_mpi -s tpr_NP3T_eq.tpr -c gro_NP3T_eq.gro -g log_NP3T_eq.log -e edr_NP3T_eq.edr -x xtc_NP3T_eq.xtc

gmx grompp -f mdp_NP6T_eq.mdp -c gro_NP3T_eq.gro -p topol.top -o tpr_NP6T_eq.tpr
gerun mdrun_mpi -s tpr_NP6T_eq.tpr -c gro_NP6T_eq.gro -g log_NP6T_eq.log -e edr_NP6T_eq.edr -x xtc_NP6T_eq.xtc

gmx grompp -f mdp_NP6T_tau-p-8_K.mdp -c gro_NP6T_eq.gro -p topol.top -o tpr_NP6T_tau-p-8_K.tpr
gerun mdrun_mpi -s tpr_NP6T_tau-p-8_K.tpr -c gro_NP6T_tau-p-8_K.gro -g log_NP6T_tau-p-8_K.log -e edr_NP6T_tau-p-8_K.edr -x xtc_NP6T_tau-p-8_K.xtc

gmx grompp -f mdp_NP6T_tau-p-6_K.mdp -c gro_NP6T_eq.gro -p topol.top -o tpr_NP6T_tau-p-6_K.tpr
gerun mdrun_mpi -s tpr_NP6T_tau-p-6_K.tpr -c gro_NP6T_tau-p-6_K.gro -g log_NP6T_tau-p-6_K.log -e edr_NP6T_tau-p-6_K.edr -x xtc_NP6T_tau-p-6_K.xtc

gmx grompp -f mdp_NP6T_tau-p-4_K.mdp -c gro_NP6T_eq.gro -p topol.top -o tpr_NP6T_tau-p-4_K.tpr
gerun mdrun_mpi -s tpr_NP6T_tau-p-4_K.tpr -c gro_NP6T_tau-p-4_K.gro -g log_NP6T_tau-p-4_K.log -e edr_NP6T_tau-p-4_K.edr -x xtc_NP6T_tau-p-4_K.xtc

gmx grompp -f mdp_NP6T_tau-p-2_K.mdp -c gro_NP6T_eq.gro -p topol.top -o tpr_NP6T_tau-p-2_K.tpr
gerun mdrun_mpi -s tpr_NP6T_tau-p-2_K.tpr -c gro_NP6T_tau-p-2_K.gro -g log_NP6T_tau-p-2_K.log -e edr_NP6T_tau-p-2_K.edr -x xtc_NP6T_tau-p-2_K.xtc
