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

gmx grompp -f mdp_NPT_eq.mdp -c 1024xC16_4nsEq-FW7L_shiftCC-0.017_no-vel.gro -p topol_0.004.top -o tpr_NPT_eq.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc -table tables/table_0.004.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq.gro -p topol_0.004.top -o tpr_NPT_sim_0.004.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.004.tpr -c gro_NPT_sim_0.004.gro -g log_NPT_sim_0.004.log -e edr_NPT_sim_0.004.edr -x xtc_NPT_sim_0.004.xtc -table tables/table_0.004.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.004.gro -p topol_0.006.top -o tpr_NPT_sim_0.006.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.006.tpr -c gro_NPT_sim_0.006.gro -g log_NPT_sim_0.006.log -e edr_NPT_sim_0.006.edr -x xtc_NPT_sim_0.006.xtc -table tables/table_0.006.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.006.gro -p topol_0.008.top -o tpr_NPT_sim_0.008.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim_0.008.tpr -c gro_NPT_sim_0.008.gro -g log_NPT_sim_0.008.log -e edr_NPT_sim_0.008.edr -x xtc_NPT_sim_0.008.xtc -table tables/table_0.008.xvg

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_sim_0.008.gro -p topol_0.010.top -o tpr_NPT_sim_0.010.tpr -n index.ndx
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