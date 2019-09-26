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

gmx grompp -f mdp_NPT_anneal_270-170K.mdp -c 2048xC8-UA_14nsEq-TraPPE -p topol.top -o tpr_NPT_anneal_270-170K.tpr
gmx mdrun -s tpr_NPT_anneal_270-170K.tpr -c gro_NPT_anneal_270-170K.gro -g log_NPT_anneal_270-170K.log -e edr_NPT_anneal_270-170K.edr -x xtc_NPT_anneal_270-170K.xtc

gmx grompp -f mdp_NPT_anneal_170-270K.mdp -c gro_NPT_anneal_270-170K.gro -p topol.top -o tpr_NPT_anneal_170-270K.tpr
gmx mdrun -s tpr_NPT_anneal_170-270K.tpr -c gro_NPT_anneal_170-270K.gro -g log_NPT_anneal_170-270K.log -e edr_NPT_anneal_170-270K.edr -x xtc_NPT_anneal_170-270K.xtc
