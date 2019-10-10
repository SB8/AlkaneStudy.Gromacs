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

gmx grompp -f mdp_NPT_285K_2.mdp -c gro_NPTeq_280K_100ps_multiphase.gro -p topol.top -o tpr_NPT_285K_2.tpr
gmx mdrun -s tpr_NPT_285K_2.tpr -c gro_NPT_285K_2.gro -g log_NPT_285K_2.log -e edr_NPT_285K_2.edr -x xtc_NPT_285K_2.xtc

gmx grompp -f mdp_NPT_295K_2.mdp -c gro_NPTeq_280K_100ps_multiphase.gro -p topol.top -o tpr_NPT_295K_2.tpr
gmx mdrun -s tpr_NPT_295K_2.tpr -c gro_NPT_295K_2.gro -g log_NPT_295K_2.log -e edr_NPT_295K_2.edr -x xtc_NPT_295K_2.xtc
