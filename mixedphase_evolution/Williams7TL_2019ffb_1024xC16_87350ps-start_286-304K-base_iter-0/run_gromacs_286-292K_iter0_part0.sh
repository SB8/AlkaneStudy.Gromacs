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

gmx grompp -f mdp_NVT_286K.mdp -c gro_240-340K_37350ps.gro -p topol.top -o tpr_NVT_286K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NVT_286K.tpr -c gro_NVT_286K.gro -g log_NVT_286K.log -e edr_NVT_286K.edr -x xtc_NVT_286K.xtc -table table.xvg

gmx grompp -f mdp_NPTeq_286K.mdp -c gro_NVT_286K.gro -p topol.top -o tpr_NPTeq_286K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPTeq_286K.tpr -c gro_NPTeq_286K.gro -g log_NPTeq_286K.log -e edr_NPTeq_286K.edr -x xtc_NPTeq_286K.xtc -table table.xvg

gmx grompp -f mdp_NPT_286K_0.mdp -c gro_NPTeq_286K.gro -p topol.top -o tpr_NPT_286K_0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_286K_0.tpr -c gro_NPT_286K_0.gro -g log_NPT_286K_0.log -e edr_NPT_286K_0.edr -x xtc_NPT_286K_0.xtc -table table.xvg

gmx grompp -f mdp_NVT_292K.mdp -c gro_240-340K_37350ps.gro -p topol.top -o tpr_NVT_292K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NVT_292K.tpr -c gro_NVT_292K.gro -g log_NVT_292K.log -e edr_NVT_292K.edr -x xtc_NVT_292K.xtc -table table.xvg

gmx grompp -f mdp_NPTeq_292K.mdp -c gro_NVT_292K.gro -p topol.top -o tpr_NPTeq_292K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPTeq_292K.tpr -c gro_NPTeq_292K.gro -g log_NPTeq_292K.log -e edr_NPTeq_292K.edr -x xtc_NPTeq_292K.xtc -table table.xvg

gmx grompp -f mdp_NPT_292K_0.mdp -c gro_NPTeq_292K.gro -p topol.top -o tpr_NPT_292K_0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_292K_0.tpr -c gro_NPT_292K_0.gro -g log_NPT_292K_0.log -e edr_NPT_292K_0.edr -x xtc_NPT_292K_0.xtc -table table.xvg
