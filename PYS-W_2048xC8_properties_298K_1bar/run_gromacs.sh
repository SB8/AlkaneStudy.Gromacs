#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 48
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_EM.mdp -c 2048xC8_UA_start.gro -p topol.top -o tpr_EM.tpr
gerun mdrun_mpi -s tpr_EM.tpr -c gro_EM.gro -g log_EM.log -e edr_EM.edr -o trr_EM.trr

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_0.tpr
gerun mdrun_mpi -s tpr_NPT_eq_0.tpr -c gro_NPT_eq_0.gro -g log_NPT_eq_0.log -e edr_NPT_eq_0.edr -x xtc_NPT_eq_0.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_0.gro -p topol.top -o tpr_NPT_sim_0.tpr
gerun mdrun_mpi -s tpr_NPT_sim_0.tpr -c gro_NPT_sim_0.gro -g log_NPT_sim_0.log -e edr_NPT_sim_0.edr -x xtc_NPT_sim_0.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_NPT_sim_0.gro -p topol.top -o tpr_NPT_eq_1.tpr
gerun mdrun_mpi -s tpr_NPT_eq_1.tpr -c gro_NPT_eq_1.gro -g log_NPT_eq_1.log -e edr_NPT_eq_1.edr -x xtc_NPT_eq_1.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_1.gro -p topol.top -o tpr_NPT_sim_1.tpr
gerun mdrun_mpi -s tpr_NPT_sim_1.tpr -c gro_NPT_sim_1.gro -g log_NPT_sim_1.log -e edr_NPT_sim_1.edr -x xtc_NPT_sim_1.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_NPT_sim_1.gro -p topol.top -o tpr_NPT_eq_2.tpr
gerun mdrun_mpi -s tpr_NPT_eq_2.tpr -c gro_NPT_eq_2.gro -g log_NPT_eq_2.log -e edr_NPT_eq_2.edr -x xtc_NPT_eq_2.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_2.gro -p topol.top -o tpr_NPT_sim_2.tpr
gerun mdrun_mpi -s tpr_NPT_sim_2.tpr -c gro_NPT_sim_2.gro -g log_NPT_sim_2.log -e edr_NPT_sim_2.edr -x xtc_NPT_sim_2.xtc

sleep 1
python3 box_resize.py gmx NPT_sim_2 3 gro_interface_start.gro
sleep 1

gmx grompp -f mdp_NVT_interface.mdp -c gro_interface_start.gro -p topol.top -o tpr_NVT_interface.tpr
gerun mdrun_mpi -s tpr_NVT_interface.tpr -c gro_NVT_interface.gro -g log_NVT_interface.log -e edr_NVT_interface.edr -x xtc_NVT_interface.xtc
