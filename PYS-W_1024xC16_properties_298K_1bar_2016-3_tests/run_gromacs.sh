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

module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_EM.mdp -c 1024xC16_UA_start.gro -p topol.top -o tpr_EM.tpr
gerun mdrun_mpi -s tpr_EM.tpr -c gro_EM.gro -g log_EM.log -e edr_EM.edr -o trr_EM.trr 

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq.tpr
gerun mdrun_mpi -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc 

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_sim.tpr
gerun mdrun_mpi -s tpr_NPT_sim.tpr -c gro_NPT_sim.gro -g log_NPT_sim.log -e edr_NPT_sim.edr -x xtc_NPT_sim.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0025.mdp -c gro_NPT_sim.gro -p topol.top -o tpr_NPT_cosacc_0.0025.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0025.tpr -c gro_NPT_cosacc_0.0025.gro -g log_NPT_cosacc_0.0025.log -e edr_NPT_cosacc_0.0025.edr -x xtc_NPT_cosacc_0.0025.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0035.mdp -c gro_NPT_cosacc_0.0025.gro -p topol.top -o tpr_NPT_cosacc_0.0035.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0035.tpr -c gro_NPT_cosacc_0.0035.gro -g log_NPT_cosacc_0.0035.log -e edr_NPT_cosacc_0.0035.edr -x xtc_NPT_cosacc_0.0035.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0050.mdp -c gro_NPT_cosacc_0.0035.gro -p topol.top -o tpr_NPT_cosacc_0.0050.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0050.tpr -c gro_NPT_cosacc_0.0050.gro -g log_NPT_cosacc_0.0050.log -e edr_NPT_cosacc_0.0050.edr -x xtc_NPT_cosacc_0.0050.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0071.mdp -c gro_NPT_cosacc_0.0050.gro -p topol.top -o tpr_NPT_cosacc_0.0071.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0071.tpr -c gro_NPT_cosacc_0.0071.gro -g log_NPT_cosacc_0.0071.log -e edr_NPT_cosacc_0.0071.edr -x xtc_NPT_cosacc_0.0071.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0100.mdp -c gro_NPT_cosacc_0.0071.gro -p topol.top -o tpr_NPT_cosacc_0.0100.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0100.tpr -c gro_NPT_cosacc_0.0100.gro -g log_NPT_cosacc_0.0100.log -e edr_NPT_cosacc_0.0100.edr -x xtc_NPT_cosacc_0.0100.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0141.mdp -c gro_NPT_cosacc_0.0100.gro -p topol.top -o tpr_NPT_cosacc_0.0141.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0141.tpr -c gro_NPT_cosacc_0.0141.gro -g log_NPT_cosacc_0.0141.log -e edr_NPT_cosacc_0.0141.edr -x xtc_NPT_cosacc_0.0141.xtc 

gmx grompp -f mdp_NPT_cosacc_0.0200.mdp -c gro_NPT_cosacc_0.0141.gro -p topol.top -o tpr_NPT_cosacc_0.0200.tpr
gerun mdrun_mpi -s tpr_NPT_cosacc_0.0200.tpr -c gro_NPT_cosacc_0.0200.gro -g log_NPT_cosacc_0.0200.log -e edr_NPT_cosacc_0.0200.edr -x xtc_NPT_cosacc_0.0200.xtc 
