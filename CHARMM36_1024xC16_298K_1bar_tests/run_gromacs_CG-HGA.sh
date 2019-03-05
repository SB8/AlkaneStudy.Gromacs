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

module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_sim_CG-HGA.mdp -c 1024xC16-AA_2nsEq-L-OPLS.gro -p topol_CG-HGA.top -o tpr_NPT_sim_CG-HGA.tpr
gerun mdrun_mpi -s tpr_NPT_sim_CG-HGA.tpr  -c gro_NPT_sim_CG-HGA.gro -g log_NPT_sim_CG-HGA.log -e edr_NPT_sim_CG-HGA.edr -x xtc_NPT_sim_CG-HGA.xtc
