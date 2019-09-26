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

gmx grompp -f mdp_EM.mdp -c 1024xC15-AA_3nsEq-CHARMM36 -p topol.top -o tpr_EM.tpr
gerun mdrun_mpi -s tpr_EM.tpr -c gro_EM.gro -g log_EM.log -e edr_EM.edr -o trr_EM.trr

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_0.tpr
gerun mdrun_mpi -s tpr_NPT_eq_0.tpr -c gro_NPT_eq_0.gro -g log_NPT_eq_0.log -e edr_NPT_eq_0.edr -x xtc_NPT_eq_0.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_0.gro -p topol.top -o tpr_NPT_sim_0.tpr
gerun mdrun_mpi -s tpr_NPT_sim_0.tpr -c gro_NPT_sim_0.gro -g log_NPT_sim_0.log -e edr_NPT_sim_0.edr -x xtc_NPT_sim_0.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_1.tpr
gerun mdrun_mpi -s tpr_NPT_eq_1.tpr -c gro_NPT_eq_1.gro -g log_NPT_eq_1.log -e edr_NPT_eq_1.edr -x xtc_NPT_eq_1.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_1.gro -p topol.top -o tpr_NPT_sim_1.tpr
gerun mdrun_mpi -s tpr_NPT_sim_1.tpr -c gro_NPT_sim_1.gro -g log_NPT_sim_1.log -e edr_NPT_sim_1.edr -x xtc_NPT_sim_1.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_2.tpr
gerun mdrun_mpi -s tpr_NPT_eq_2.tpr -c gro_NPT_eq_2.gro -g log_NPT_eq_2.log -e edr_NPT_eq_2.edr -x xtc_NPT_eq_2.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_2.gro -p topol.top -o tpr_NPT_sim_2.tpr
gerun mdrun_mpi -s tpr_NPT_sim_2.tpr -c gro_NPT_sim_2.gro -g log_NPT_sim_2.log -e edr_NPT_sim_2.edr -x xtc_NPT_sim_2.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_3.tpr
gerun mdrun_mpi -s tpr_NPT_eq_3.tpr -c gro_NPT_eq_3.gro -g log_NPT_eq_3.log -e edr_NPT_eq_3.edr -x xtc_NPT_eq_3.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_3.gro -p topol.top -o tpr_NPT_sim_3.tpr
gerun mdrun_mpi -s tpr_NPT_sim_3.tpr -c gro_NPT_sim_3.gro -g log_NPT_sim_3.log -e edr_NPT_sim_3.edr -x xtc_NPT_sim_3.xtc

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq_4.tpr
gerun mdrun_mpi -s tpr_NPT_eq_4.tpr -c gro_NPT_eq_4.gro -g log_NPT_eq_4.log -e edr_NPT_eq_4.edr -x xtc_NPT_eq_4.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq_4.gro -p topol.top -o tpr_NPT_sim_4.tpr
gerun mdrun_mpi -s tpr_NPT_sim_4.tpr -c gro_NPT_sim_4.gro -g log_NPT_sim_4.log -e edr_NPT_sim_4.edr -x xtc_NPT_sim_4.xtc

sleep 1
python3 box_resize.py gmx NPT_sim_4 3 gro_interface_start.gro
sleep 1
