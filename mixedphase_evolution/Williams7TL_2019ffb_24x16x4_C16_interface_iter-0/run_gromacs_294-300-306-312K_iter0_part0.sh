#$ -S /bin/bash
#$ -l h_rt=23:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 96
#$ -P Gold
#$ -A QMUL_BURROWS
#$ -cwd
#$ -e /dev/null

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NP3T_294K_4.0ns_iter0.mdp -c gro_NP6T_306K.gro -p topol.top -o tpr_NP3T_294K_4.0ns_iter0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NP3T_294K_4.0ns_iter0.tpr -c gro_NP3T_294K_4.0ns_iter0.gro -g log_NP3T_294K_4.0ns_iter0.log -e edr_NP3T_294K_4.0ns_iter0.edr -x xtc_NP3T_294K_4.0ns_iter0.xtc -table table.xvg

gmx grompp -f mdp_NP3T_300K_4.0ns_iter0.mdp -c gro_NP6T_306K.gro -p topol.top -o tpr_NP3T_300K_4.0ns_iter0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NP3T_300K_4.0ns_iter0.tpr -c gro_NP3T_300K_4.0ns_iter0.gro -g log_NP3T_300K_4.0ns_iter0.log -e edr_NP3T_300K_4.0ns_iter0.edr -x xtc_NP3T_300K_4.0ns_iter0.xtc -table table.xvg

gmx grompp -f mdp_NP3T_306K_4.0ns_iter0.mdp -c gro_NP6T_306K.gro -p topol.top -o tpr_NP3T_306K_4.0ns_iter0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NP3T_306K_4.0ns_iter0.tpr -c gro_NP3T_306K_4.0ns_iter0.gro -g log_NP3T_306K_4.0ns_iter0.log -e edr_NP3T_306K_4.0ns_iter0.edr -x xtc_NP3T_306K_4.0ns_iter0.xtc -table table.xvg

gmx grompp -f mdp_NP3T_312K_4.0ns_iter0.mdp -c gro_NP6T_306K.gro -p topol.top -o tpr_NP3T_312K_4.0ns_iter0.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NP3T_312K_4.0ns_iter0.tpr -c gro_NP3T_312K_4.0ns_iter0.gro -g log_NP3T_312K_4.0ns_iter0.log -e edr_NP3T_312K_4.0ns_iter0.edr -x xtc_NP3T_312K_4.0ns_iter0.xtc -table table.xvg
