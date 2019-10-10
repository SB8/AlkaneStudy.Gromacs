#$ -S /bin/bash
#$ -l h_rt=48:00:00
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

gmx grompp -f mdp_NPT_270K.mdp -c gro_NPT_eq_288.gro -p topol.top -o tpr_NPT_270K_0.tpr
gmx mdrun -s tpr_NPT_270K_0.tpr -c gro_NPT_270K_0.gro -g log_NPT_270K_0.log -e edr_NPT_270K_0.edr -x xtc_NPT_270K_0.xtc

gmx grompp -f mdp_NPT_280K.mdp -c gro_NPT_eq_288.gro -p topol.top -o tpr_NPT_280K_0.tpr
gmx mdrun -s tpr_NPT_280K_0.tpr -c gro_NPT_280K_0.gro -g log_NPT_280K_0.log -e edr_NPT_280K_0.edr -x xtc_NPT_280K_0.xtc

gmx grompp -f mdp_NPT_290K.mdp -c gro_NPT_eq_288.gro -p topol.top -o tpr_NPT_290K_0.tpr
gmx mdrun -s tpr_NPT_290K_0.tpr -c gro_NPT_290K_0.gro -g log_NPT_290K_0.log -e edr_NPT_290K_0.edr -x xtc_NPT_290K_0.xtc

gmx grompp -f mdp_NPT_300K.mdp -c gro_NPT_eq_288.gro -p topol.top -o tpr_NPT_300K_0.tpr
gmx mdrun -s tpr_NPT_300K_0.tpr -c gro_NPT_300K_0.gro -g log_NPT_300K_0.log -e edr_NPT_300K_0.edr -x xtc_NPT_300K_0.xtc

gmx grompp -f mdp_NPT_310K.mdp -c gro_NPT_eq_288.gro -p topol.top -o tpr_NPT_310K_0.tpr
gmx mdrun -s tpr_NPT_310K_0.tpr -c gro_NPT_310K_0.gro -g log_NPT_310K_0.log -e edr_NPT_310K_0.edr -x xtc_NPT_310K_0.xtc
