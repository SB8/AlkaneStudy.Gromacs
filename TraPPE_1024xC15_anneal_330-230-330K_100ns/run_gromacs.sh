#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 72
#$ -P Gold
#$ -A QMUL_BOEK
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_anneal_330-230K.mdp -c 1024xC15-UA_4nsEq-TraPPE.gro -p topol.top -o tpr_NPT_anneal_330-230K.tpr
gmx mdrun -s tpr_NPT_anneal_330-230K.tpr -c gro_NPT_anneal_330-230K.gro -g log_NPT_anneal_330-230K.log -e edr_NPT_anneal_330-230K.edr -x xtc_NPT_anneal_330-230K.xtc

gmx grompp -f mdp_NPT_anneal_230-330K.mdp -c gro_NPT_anneal_330-230K.gro -p topol.top -o tpr_NPT_anneal_230-330K.tpr
gmx mdrun -s tpr_NPT_anneal_230-330K.tpr -c gro_NPT_anneal_230-330K.gro -g log_NPT_anneal_230-330K.log -e edr_NPT_anneal_230-330K.edr -x xtc_NPT_anneal_230-330K.xtc
