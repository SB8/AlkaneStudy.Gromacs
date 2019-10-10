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

gmx grompp -f mdp_NPT_eq_280.mdp -c gro_NPT_anneal_340-240K_41-90.gro -p topol.top -o tpr_NPT_eq_280.tpr
gmx mdrun -s tpr_NPT_eq_280.tpr -c gro_NPT_eq_280.gro -g log_NPT_eq_280.log -e edr_NPT_eq_280.edr -x xtc_NPT_eq_280.xtc -o trr_NPT_eq_280.trr
