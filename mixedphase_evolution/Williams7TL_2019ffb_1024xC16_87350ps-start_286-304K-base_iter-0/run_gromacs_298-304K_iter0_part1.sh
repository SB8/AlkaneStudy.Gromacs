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

gmx grompp -f mdp_NVT_298K.mdp -c gro_240-340K_37350ps.gro -p topol.top -o tpr_NVT_298K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NVT_298K.tpr -c gro_NVT_298K.gro -g log_NVT_298K.log -e edr_NVT_298K.edr -x xtc_NVT_298K.xtc -table table.xvg

gmx grompp -f mdp_NPTeq_298K.mdp -c gro_NVT_298K.gro -p topol.top -o tpr_NPTeq_298K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPTeq_298K.tpr -c gro_NPTeq_298K.gro -g log_NPTeq_298K.log -e edr_NPTeq_298K.edr -x xtc_NPTeq_298K.xtc -table table.xvg

gmx grompp -f mdp_NPT_298K_0.mdp -c gro_NPTeq_298K.gro -p topol.top -o tpr_NPT_298K_0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_298K_0.tpr -c gro_NPT_298K_0.gro -g log_NPT_298K_0.log -e edr_NPT_298K_0.edr -x xtc_NPT_298K_0.xtc -table table.xvg

gmx grompp -f mdp_NVT_304K.mdp -c gro_240-340K_37350ps.gro -p topol.top -o tpr_NVT_304K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NVT_304K.tpr -c gro_NVT_304K.gro -g log_NVT_304K.log -e edr_NVT_304K.edr -x xtc_NVT_304K.xtc -table table.xvg

gmx grompp -f mdp_NPTeq_304K.mdp -c gro_NVT_304K.gro -p topol.top -o tpr_NPTeq_304K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPTeq_304K.tpr -c gro_NPTeq_304K.gro -g log_NPTeq_304K.log -e edr_NPTeq_304K.edr -x xtc_NPTeq_304K.xtc -table table.xvg

gmx grompp -f mdp_NPT_304K_0.mdp -c gro_NPTeq_304K.gro -p topol.top -o tpr_NPT_304K_0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_304K_0.tpr -c gro_NPT_304K_0.gro -g log_NPT_304K_0.log -e edr_NPT_304K_0.edr -x xtc_NPT_304K_0.xtc -table table.xvg
