#$ -S /bin/bash
#$ -l h_rt=48:00:00
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

gmx grompp -f mdp_NPT_anneal_283-333-283K.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_anneal_283-333-283K.tpr
gerun mdrun_mpi -s tpr_NPT_anneal_283-333-283K.tpr -c gro_NPT_anneal_283-333-283K.gro -g log_NPT_anneal_283-333-283K.log -e edr_NPT_anneal_283-333-283K.edr -x xtc_NPT_anneal_283-333-283K.xtc
