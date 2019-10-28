#$ -S /bin/bash
#$ -l h_rt=48:00:00
#$ -l mem=4G
#$ -l tmpfs=10G
#$ -N GROMACS
#$ -pe mpi 72
#$ -P Gold
#$ -A QMUL_SMOUKOV
#$ -cwd

module unload compilers/intel/2018/update3
module unload mpi/intel/2018/update3/intel

module load python3
module load compilers/intel/2017/update1
module load mpi/intel/2017/update1/intel
module load gromacs/2016.3/intel-2017-update1

gmx grompp -f mdp_NPT_anneal_340-240K.mdp -c 1024xC16-AA_5nsEq_FlexWilliams.gro -p topol_0.011.top -o tpr_NPT_anneal_340-240K.tpr -n index.ndx
gerun mdrun_mpi -s tpr_NPT_anneal_340-240K.tpr -c gro_NPT_anneal_340-240K.gro -g log_NPT_anneal_340-240K.log -e edr_NPT_anneal_340-240K.edr -x xtc_NPT_anneal_340-240K.xtc -table tables/table_0.011.xvg
