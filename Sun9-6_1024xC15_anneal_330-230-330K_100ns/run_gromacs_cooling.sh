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

gmx grompp -f mdp_NPT_anneal_330-230K.mdp -c 1024xC15-AA_4nsEq-Sun9-6.gro -p topol.top -o tpr_NPT_anneal_330-230K.tpr
gerun mdrun_mpi -s tpr_NPT_anneal_330-230K.tpr -c gro_NPT_anneal_330-230K.gro -g log_NPT_anneal_330-230K.log -e edr_NPT_anneal_330-230K.edr -x xtc_NPT_anneal_330-230K.xtc -table table6-9.xvg
