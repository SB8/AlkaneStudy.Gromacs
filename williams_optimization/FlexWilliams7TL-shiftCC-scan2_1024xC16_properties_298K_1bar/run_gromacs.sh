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

gmx grompp -f mdp_NPT_eq.mdp -c 1024xC16_4nsEq-FW7L_shiftCC-0.017_no-vel.gro -p topol_0.020.top -o tpr_NPT_eq.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc -table tables/table_0.000.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq.gro -p topol_0.020.top -o tpr_NPT_sim_0.020.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.020.tpr -c gro_NPT_sim_0.020.gro -g log_NPT_sim_0.020.log -e edr_NPT_sim_0.020.edr -x xtc_NPT_sim_0.020.xtc -table tables/table_0.020.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.020.gro -p topol_0.022.top -o tpr_NPT_sim_0.022.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.022.tpr -c gro_NPT_sim_0.022.gro -g log_NPT_sim_0.022.log -e edr_NPT_sim_0.022.edr -x xtc_NPT_sim_0.022.xtc -table tables/table_0.022.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.022.gro -p topol_0.024.top -o tpr_NPT_sim_0.024.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.024.tpr -c gro_NPT_sim_0.024.gro -g log_NPT_sim_0.024.log -e edr_NPT_sim_0.024.edr -x xtc_NPT_sim_0.024.xtc -table tables/table_0.024.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.024.gro -p topol_0.026.top -o tpr_NPT_sim_0.026.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.026.tpr -c gro_NPT_sim_0.026.gro -g log_NPT_sim_0.026.log -e edr_NPT_sim_0.026.edr -x xtc_NPT_sim_0.026.xtc -table tables/table_0.026.xvg
