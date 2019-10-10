#$ -S /bin/bash
#$ -l h_rt=23:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 72
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NVT_eq_292K.mdp -c gro_240-340K_37350ps.gro -p topol.top -o tpr_NVT_eq_292K.tpr -n index.ndx
gmx mdrun -s tpr_NVT_eq_292K.tpr -c gro_NVT_eq_292K.gro -g log_NVT_eq_292K.log -e edr_NVT_eq_292K.edr -x xtc_NVT_eq_292K.xtc -table table.xvg

gmx grompp -f mdp_NPT_eq_292K.mdp -c gro_NVT_eq_292K.gro -p topol.top -o tpr_NPT_eq_292K.tpr -n index.ndx
gmx mdrun -s tpr_NPT_eq_292K.tpr -c gro_NPT_eq_292K.gro -g log_NPT_eq_292K.log -e edr_NPT_eq_292K.edr -x xtc_NPT_eq_292K.xtc -table table.xvg
