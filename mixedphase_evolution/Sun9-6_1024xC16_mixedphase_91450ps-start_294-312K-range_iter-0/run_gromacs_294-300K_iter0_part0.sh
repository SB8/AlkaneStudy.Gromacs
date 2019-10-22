#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 120
#$ -P Gold
#$ -A QMUL_SMOUKOV
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NVT_294K.mdp -c Sun9-6_1024xC16_240-340K_41450ps.gro -p topol.top -o tpr_NVT_294K.tpr
gerun mdrun_mpi -s tpr_NVT_294K.tpr -c gro_NVT_294K.gro -g log_NVT_294K.log -e edr_NVT_294K.edr -x xtc_NVT_294K.xtc -table table6-9.xvg

gmx grompp -f mdp_NPTeq_294K.mdp -c gro_NVT_294K.gro -p topol.top -o tpr_NPTeq_294K.tpr
gerun mdrun_mpi -s tpr_NPTeq_294K.tpr -c gro_NPTeq_294K.gro -g log_NPTeq_294K.log -e edr_NPTeq_294K.edr -x xtc_NPTeq_294K.xtc -table table6-9.xvg

gmx grompp -f mdp_NPT_294K_0.mdp -c gro_NPTeq_294K.gro -p topol.top -o tpr_NPT_294K_0.tpr
gerun mdrun_mpi -s tpr_NPT_294K_0.tpr -c gro_NPT_294K_0.gro -g log_NPT_294K_0.log -e edr_NPT_294K_0.edr -x xtc_NPT_294K_0.xtc -table table6-9.xvg

gmx grompp -f mdp_NVT_300K.mdp -c Sun9-6_1024xC16_240-340K_41450ps.gro -p topol.top -o tpr_NVT_300K.tpr
gerun mdrun_mpi -s tpr_NVT_300K.tpr -c gro_NVT_300K.gro -g log_NVT_300K.log -e edr_NVT_300K.edr -x xtc_NVT_300K.xtc -table table6-9.xvg

gmx grompp -f mdp_NPTeq_300K.mdp -c gro_NVT_300K.gro -p topol.top -o tpr_NPTeq_300K.tpr
gerun mdrun_mpi -s tpr_NPTeq_300K.tpr -c gro_NPTeq_300K.gro -g log_NPTeq_300K.log -e edr_NPTeq_300K.edr -x xtc_NPTeq_300K.xtc -table table6-9.xvg

gmx grompp -f mdp_NPT_300K_0.mdp -c gro_NPTeq_300K.gro -p topol.top -o tpr_NPT_300K_0.tpr
gerun mdrun_mpi -s tpr_NPT_300K_0.tpr -c gro_NPT_300K_0.gro -g log_NPT_300K_0.log -e edr_NPT_300K_0.edr -x xtc_NPT_300K_0.xtc -table table6-9.xvg
