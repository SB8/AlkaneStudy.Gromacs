#$ -S /bin/bash
#$ -l h_rt=48:00:00
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

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_3.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_eq_3.tpr -c gro_NPT_eq_3.gro -g log_NPT_eq_3.log -e edr_NPT_eq_3.edr -x xtc_NPT_eq_3.xtc -table table.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_3.gro -p topol.top -o tpr_NPT_sim_3.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_3.tpr -c gro_NPT_sim_3.gro -g log_NPT_sim_3.log -e edr_NPT_sim_3.edr -x xtc_NPT_sim_3.xtc -table table.xvg

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_4.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_eq_4.tpr -c gro_NPT_eq_4.gro -g log_NPT_eq_4.log -e edr_NPT_eq_4.edr -x xtc_NPT_eq_4.xtc -table table.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_4.gro -p topol.top -o tpr_NPT_sim_4.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_4.tpr -c gro_NPT_sim_4.gro -g log_NPT_sim_4.log -e edr_NPT_sim_4.edr -x xtc_NPT_sim_4.xtc -table table.xvg
