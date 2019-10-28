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

gmx grompp -f mdp_NVT_306K.mdp -c Sun9-6_1024xC16_240-340K_41450ps.gro -p topol.top -o tpr_NVT_306K.tpr
gerun mdrun_mpi -s tpr_NVT_306K.tpr -c gro_NVT_306K.gro -g log_NVT_306K.log -e edr_NVT_306K.edr -x xtc_NVT_306K.xtc

gmx grompp -f mdp_NPTeq_306K.mdp -c gro_NVT_306K.gro -p topol.top -o tpr_NPTeq_306K.tpr
gerun mdrun_mpi -s tpr_NPTeq_306K.tpr -c gro_NPTeq_306K.gro -g log_NPTeq_306K.log -e edr_NPTeq_306K.edr -x xtc_NPTeq_306K.xtc

gmx grompp -f mdp_NPT_306K_0.mdp -c gro_NPTeq_306K.gro -p topol.top -o tpr_NPT_306K_0.tpr
gerun mdrun_mpi -s tpr_NPT_306K_0.tpr -c gro_NPT_306K_0.gro -g log_NPT_306K_0.log -e edr_NPT_306K_0.edr -x xtc_NPT_306K_0.xtc

gmx grompp -f mdp_NVT_312K.mdp -c Sun9-6_1024xC16_240-340K_41450ps.gro -p topol.top -o tpr_NVT_312K.tpr
gerun mdrun_mpi -s tpr_NVT_312K.tpr -c gro_NVT_312K.gro -g log_NVT_312K.log -e edr_NVT_312K.edr -x xtc_NVT_312K.xtc

gmx grompp -f mdp_NPTeq_312K.mdp -c gro_NVT_312K.gro -p topol.top -o tpr_NPTeq_312K.tpr
gerun mdrun_mpi -s tpr_NPTeq_312K.tpr -c gro_NPTeq_312K.gro -g log_NPTeq_312K.log -e edr_NPTeq_312K.edr -x xtc_NPTeq_312K.xtc

gmx grompp -f mdp_NPT_312K_0.mdp -c gro_NPTeq_312K.gro -p topol.top -o tpr_NPT_312K_0.tpr
gerun mdrun_mpi -s tpr_NPT_312K_0.tpr -c gro_NPT_312K_0.gro -g log_NPT_312K_0.log -e edr_NPT_312K_0.edr -x xtc_NPT_312K_0.xtc
