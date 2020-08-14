#$ -S /bin/bash
#$ -l h_rt=12:00:00
#$ -l mem=8G
#$ -l tmpfs=5G
#$ -N GROMACS
#$ -pe mpi 48
#$ -P Free
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1


gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.028.gro -p topol_0.030.top -o tpr_NPT_sim_0.030.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.030.tpr -c gro_NPT_sim_0.030.gro -g log_NPT_sim_0.030.log -e edr_NPT_sim_0.030.edr -x xtc_NPT_sim_0.030.xtc -table tables/table_0.030.xvg
