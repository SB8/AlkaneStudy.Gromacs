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

gmx grompp -f mdp_NPT_eq.mdp -c 1024xC15-AA_14nsEq-FWL4_no-vel.gro -p topol_0.000.top -o tpr_NPT_eq.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc -table tables/table_0.000.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq.gro -p topol_0.000.top -o tpr_NPT_sim_0.000.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.000.tpr -c gro_NPT_sim_0.000.gro -g log_NPT_sim_0.000.log -e edr_NPT_sim_0.000.edr -x xtc_NPT_sim_0.000.xtc -table tables/table_0.000.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.000.gro -p topol_0.002.top -o tpr_NPT_sim_0.002.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.002.tpr -c gro_NPT_sim_0.002.gro -g log_NPT_sim_0.002.log -e edr_NPT_sim_0.002.edr -x xtc_NPT_sim_0.002.xtc -table tables/table_0.002.xvg

