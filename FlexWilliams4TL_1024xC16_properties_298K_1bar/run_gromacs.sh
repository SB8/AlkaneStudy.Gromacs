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

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_sim.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_sim.tpr -c gro_NPT_sim.gro -g log_NPT_sim.log -e edr_NPT_sim.edr -x xtc_NPT_sim.xtc -table table.xvg

sleep 1
python3 box_resize.py gmx gro_NPT_sim.gro 3 gro_interface_start.gro
sleep 1

gmx grompp -f mdp_NVT_interface.mdp -c gro_interface_start.gro -p topol.top -o tpr_NVT_interface.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NVT_interface.tpr -c gro_NVT_interface.gro -g log_NVT_interface.log -e edr_NVT_interface.edr -x xtc_NVT_interface.xtc -table table.xvg
