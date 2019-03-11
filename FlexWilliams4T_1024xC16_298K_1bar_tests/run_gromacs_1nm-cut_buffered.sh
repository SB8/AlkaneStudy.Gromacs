#$ -S /bin/bash
#$ -l h_rt=8:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 96
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_sim_1nm-cut_buffered.mdp -c 1024xC16-AA_5nsEq-FlexWilliams.gro -p topol.top -o tpr_NPT_sim_1nm-cut_buffered.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_1nm-cut_buffered.tpr  -c gro_NPT_sim_1nm-cut_buffered.gro -g log_NPT_sim_1nm-cut_buffered.log -e edr_NPT_sim_1nm-cut_buffered.edr -x xtc_NPT_sim_1nm-cut_buffered.xtc -table table.xvg
