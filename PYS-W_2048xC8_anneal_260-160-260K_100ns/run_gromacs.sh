#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 48
#$ -P Gold
#$ -A QMUL_SMOUKOV
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_anneal_260-160K.mdp -c 2048xC8-UA_4nsEq-PYS.gro -p topol.top -o tpr_NPT_anneal_260-160K.tpr
gmx mdrun -s tpr_NPT_anneal_260-160K.tpr -c gro_NPT_anneal_260-160K.gro -g log_NPT_anneal_260-160K.log -e edr_NPT_anneal_260-160K.edr -x xtc_NPT_anneal_260-160K.xtc

gmx grompp -f mdp_NPT_anneal_160-260K.mdp -c gro_NPT_anneal_260-160K.gro -p topol.top -o tpr_NPT_anneal_160-260K.tpr
gmx mdrun -s tpr_NPT_anneal_160-260K.tpr -c gro_NPT_anneal_160-260K.gro -g log_NPT_anneal_160-260K.log -e edr_NPT_anneal_160-260K.edr -x xtc_NPT_anneal_160-260K.xtc
