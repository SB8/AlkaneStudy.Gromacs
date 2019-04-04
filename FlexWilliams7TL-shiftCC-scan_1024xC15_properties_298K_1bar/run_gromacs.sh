#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 96
#$ -P Gold
#$ -A QMUL_SMOUKOV
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_sim.mdp -c 1024xC15-AA_14nsEq-FWL4.gro -p topol_0.010.top -o tpr_NPT_sim_0.010.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.010.tpr -c gro_NPT_sim_0.010.gro -g log_NPT_sim_0.010.log -e edr_NPT_sim_0.010.edr -x xtc_NPT_sim_0.010.xtc -table tables/table_0.010.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.010.gro -p topol_0.012.top -o tpr_NPT_sim_0.012.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.012.tpr -c gro_NPT_sim_0.012.gro -g log_NPT_sim_0.012.log -e edr_NPT_sim_0.012.edr -x xtc_NPT_sim_0.012.xtc -table tables/table_0.012.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.012.gro -p topol_0.014.top -o tpr_NPT_sim_0.014.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.014.tpr -c gro_NPT_sim_0.014.gro -g log_NPT_sim_0.014.log -e edr_NPT_sim_0.014.edr -x xtc_NPT_sim_0.014.xtc -table tables/table_0.014.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.014.gro -p topol_0.016.top -o tpr_NPT_sim_0.016.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.016.tpr -c gro_NPT_sim_0.016.gro -g log_NPT_sim_0.016.log -e edr_NPT_sim_0.016.edr -x xtc_NPT_sim_0.016.xtc -table tables/table_0.016.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.016.gro -p topol_0.018.top -o tpr_NPT_sim_0.018.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.018.tpr -c gro_NPT_sim_0.018.gro -g log_NPT_sim_0.018.log -e edr_NPT_sim_0.018.edr -x xtc_NPT_sim_0.018.xtc -table tables/table_0.018.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.018.gro -p topol_0.020.top -o tpr_NPT_sim_0.020.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.020.tpr -c gro_NPT_sim_0.020.gro -g log_NPT_sim_0.020.log -e edr_NPT_sim_0.020.edr -x xtc_NPT_sim_0.020.xtc -table tables/table_0.020.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.020.gro -p topol_0.022.top -o tpr_NPT_sim_0.022.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.022.tpr -c gro_NPT_sim_0.022.gro -g log_NPT_sim_0.022.log -e edr_NPT_sim_0.022.edr -x xtc_NPT_sim_0.022.xtc -table tables/table_0.022.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.022.gro -p topol_0.024.top -o tpr_NPT_sim_0.024.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.024.tpr -c gro_NPT_sim_0.024.gro -g log_NPT_sim_0.024.log -e edr_NPT_sim_0.024.edr -x xtc_NPT_sim_0.024.xtc -table tables/table_0.024.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.024.gro -p topol_0.026.top -o tpr_NPT_sim_0.026.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.026.tpr -c gro_NPT_sim_0.026.gro -g log_NPT_sim_0.026.log -e edr_NPT_sim_0.026.edr -x xtc_NPT_sim_0.026.xtc -table tables/table_0.026.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.026.gro -p topol_0.028.top -o tpr_NPT_sim_0.028.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.028.tpr -c gro_NPT_sim_0.028.gro -g log_NPT_sim_0.028.log -e edr_NPT_sim_0.028.edr -x xtc_NPT_sim_0.028.xtc -table tables/table_0.028.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.028.gro -p topol_0.030.top -o tpr_NPT_sim_0.030.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.030.tpr -c gro_NPT_sim_0.030.gro -g log_NPT_sim_0.030.log -e edr_NPT_sim_0.030.edr -x xtc_NPT_sim_0.030.xtc -table tables/table_0.030.xvg
