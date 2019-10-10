#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 96
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_wb_2fs.mdp -c 1024xC15-AA_12nsEq_L-OPLS.gro -p wb_topol.top -o tpr_NPT_wb_2fs.tpr
gerun mdrun_mpi -s tpr_NPT_wb_2fs.tpr -c gro_NPT_wb_2fs.gro -g log_NPT_wb_2fs.log -e edr_NPT_wb_2fs.edr -x xtc_NPT_wb_2fs.xtc

gmx grompp -f mdp_NPT_wb_1fs.mdp -c 1024xC15-AA_12nsEq_L-OPLS.gro -p wb_topol.top -o tpr_NPT_wb_1fs.tpr
gerun mdrun_mpi -s tpr_NPT_wb_1fs.tpr -c gro_NPT_wb_1fs.gro -g log_NPT_wb_1fs.log -e edr_NPT_wb_1fs.edr -x xtc_NPT_wb_1fs.xtc

gmx grompp -f mdp_NPT_minimal_2fs.mdp -c 1024xC15-AA_12nsEq_L-OPLS.gro -p minimal_topol.top -o tpr_NPT_minimal_2fs.tpr
gerun mdrun_mpi -s tpr_NPT_minimal_2fs.tpr -c gro_NPT_minimal_2fs.gro -g log_NPT_minimal_2fs.log -e edr_NPT_minimal_2fs.edr -x xtc_NPT_minimal_2fs.xtc

gmx grompp -f mdp_NPT_minimal_1fs.mdp -c 1024xC15-AA_12nsEq_L-OPLS.gro -p minimal_topol.top -o tpr_NPT_minimal_1fs.tpr
gerun mdrun_mpi -s tpr_NPT_minimal_1fs.tpr -c gro_NPT_minimal_1fs.gro -g log_NPT_minimal_1fs.log -e edr_NPT_minimal_1fs.edr -x xtc_NPT_minimal_1fs.xtc
