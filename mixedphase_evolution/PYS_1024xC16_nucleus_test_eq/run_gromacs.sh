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

gmx grompp -f mdp_NVTeq_360K.mdp -c C16_UA_P-1_1x1x1_unwrapped_nucleus_16x16x4_s2x2x0.gro -p topol_PR.top -o tpr_NVTeq_360K.tpr -r C16_UA_P-1_1x1x1_unwrapped_nucleus_16x16x4_s2x2x0.gro
gerun mdrun_mpi -s tpr_NVTeq_360K.tpr -c gro_NVTeq_360K.gro -g log_NVTeq_360K.log -e edr_NVTeq_360K.edr -x xtc_NVTeq_360K.xtc

gmx grompp -f mdp_NPTeq_PR_290K.mdp -c gro_NVTeq_360K.gro -p topol_PR.top -o tpr_NPTeq_PR_290K.tpr -r gro_NVTeq_360K.gro
gerun mdrun_mpi -s tpr_NPTeq_PR_290K.tpr -c gro_NPTeq_PR_290K.gro -g log_NPTeq_PR_290K.log -e edr_NPTeq_PR_290K.edr -x xtc_NPTeq_PR_290K.xtc

gmx grompp -f mdp_NPT_290K.mdp -c gro_NPTeq_PR_290K.gro -p topol.top -o tpr_NPT_290K.tpr
gerun mdrun_mpi -s tpr_NPT_290K.tpr -c gro_NPT_290K.gro -g log_NPT_290K.log -e edr_NPT_290K.edr -x xtc_NPT_290K.xtc
