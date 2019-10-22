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

gmx grompp -f mdp_NVT_284K.mdp -c gro_240-340K_32250ps.gro -p topol.top -o tpr_NVT_284K.tpr
gerun mdrun_mpi -s tpr_NVT_284K.tpr -c gro_NVT_284K.gro -g log_NVT_284K.log -e edr_NVT_284K.edr -x xtc_NVT_284K.xtc

gmx grompp -f mdp_NPTeq_284K.mdp -c gro_NVT_284K.gro -p topol.top -o tpr_NPTeq_284K.tpr
gerun mdrun_mpi -s tpr_NPTeq_284K.tpr -c gro_NPTeq_284K.gro -g log_NPTeq_284K.log -e edr_NPTeq_284K.edr -x xtc_NPTeq_284K.xtc

gmx grompp -f mdp_NPT_284K_0.mdp -c gro_NPTeq_284K.gro -p topol.top -o tpr_NPT_284K_0.tpr
gerun mdrun_mpi -s tpr_NPT_284K_0.tpr -c gro_NPT_284K_0.gro -g log_NPT_284K_0.log -e edr_NPT_284K_0.edr -x xtc_NPT_284K_0.xtc

gmx grompp -f mdp_NVT_290K.mdp -c gro_240-340K_32250ps.gro -p topol.top -o tpr_NVT_290K.tpr
gerun mdrun_mpi -s tpr_NVT_290K.tpr -c gro_NVT_290K.gro -g log_NVT_290K.log -e edr_NVT_290K.edr -x xtc_NVT_290K.xtc

gmx grompp -f mdp_NPTeq_290K.mdp -c gro_NVT_290K.gro -p topol.top -o tpr_NPTeq_290K.tpr
gerun mdrun_mpi -s tpr_NPTeq_290K.tpr -c gro_NPTeq_290K.gro -g log_NPTeq_290K.log -e edr_NPTeq_290K.edr -x xtc_NPTeq_290K.xtc

gmx grompp -f mdp_NPT_290K_0.mdp -c gro_NPTeq_290K.gro -p topol.top -o tpr_NPT_290K_0.tpr
gerun mdrun_mpi -s tpr_NPT_290K_0.tpr -c gro_NPT_290K_0.gro -g log_NPT_290K_0.log -e edr_NPT_290K_0.edr -x xtc_NPT_290K_0.xtc

gmx grompp -f mdp_NVT_296K.mdp -c gro_240-340K_32250ps.gro -p topol.top -o tpr_NVT_296K.tpr
gerun mdrun_mpi -s tpr_NVT_296K.tpr -c gro_NVT_296K.gro -g log_NVT_296K.log -e edr_NVT_296K.edr -x xtc_NVT_296K.xtc

gmx grompp -f mdp_NPTeq_296K.mdp -c gro_NVT_296K.gro -p topol.top -o tpr_NPTeq_296K.tpr
gerun mdrun_mpi -s tpr_NPTeq_296K.tpr -c gro_NPTeq_296K.gro -g log_NPTeq_296K.log -e edr_NPTeq_296K.edr -x xtc_NPTeq_296K.xtc

gmx grompp -f mdp_NPT_296K_0.mdp -c gro_NPTeq_296K.gro -p topol.top -o tpr_NPT_296K_0.tpr
gerun mdrun_mpi -s tpr_NPT_296K_0.tpr -c gro_NPT_296K_0.gro -g log_NPT_296K_0.log -e edr_NPT_296K_0.edr -x xtc_NPT_296K_0.xtc

gmx grompp -f mdp_NVT_302K.mdp -c gro_240-340K_32250ps.gro -p topol.top -o tpr_NVT_302K.tpr
gerun mdrun_mpi -s tpr_NVT_302K.tpr -c gro_NVT_302K.gro -g log_NVT_302K.log -e edr_NVT_302K.edr -x xtc_NVT_302K.xtc

gmx grompp -f mdp_NPTeq_302K.mdp -c gro_NVT_302K.gro -p topol.top -o tpr_NPTeq_302K.tpr
gerun mdrun_mpi -s tpr_NPTeq_302K.tpr -c gro_NPTeq_302K.gro -g log_NPTeq_302K.log -e edr_NPTeq_302K.edr -x xtc_NPTeq_302K.xtc

gmx grompp -f mdp_NPT_302K_0.mdp -c gro_NPTeq_302K.gro -p topol.top -o tpr_NPT_302K_0.tpr
gerun mdrun_mpi -s tpr_NPT_302K_0.tpr -c gro_NPT_302K_0.gro -g log_NPT_302K_0.log -e edr_NPT_302K_0.edr -x xtc_NPT_302K_0.xtc
