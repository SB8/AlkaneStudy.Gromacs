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

gmx grompp -f mdp_EM.mdp -c 1024xC8-UA_start.gro -p topol.top -o tpr_EM.tpr
gmx mdrun -s tpr_EM.tpr -c gro_EM.gro -g log_EM.log -e edr_EM.edr -x xtc_EM.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq.tpr
gmx mdrun -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc

gmx grompp -f mdp_NPT_anneal_280-180K.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_anneal_280-180K.tpr
gmx mdrun -s tpr_NPT_anneal_280-180K.tpr -c gro_NPT_anneal_280-180K.gro -g log_NPT_anneal_280-180K.log -e edr_NPT_anneal_280-180K.edr -x xtc_NPT_anneal_280-180K.xtc

gmx grompp -f mdp_NPT_anneal_180-280K.mdp -c gro_NPT_anneal_280-180K.gro -p topol.top -o tpr_NPT_anneal_180-280K.tpr
gmx mdrun -s tpr_NPT_anneal_180-280K.tpr -c gro_NPT_anneal_180-280K.gro -g log_NPT_anneal_180-280K.log -e edr_NPT_anneal_180-280K.edr -x xtc_NPT_anneal_180-280K.xtc
