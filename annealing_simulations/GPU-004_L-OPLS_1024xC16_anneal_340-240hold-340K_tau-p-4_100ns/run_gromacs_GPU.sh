
gmx grompp -f mdp_NPT_anneal_240-240K.mdp -c gro_NPT_anneal_340-240K.gro -p topol.top -o tpr_NPT_anneal_240-240K.tpr
gmx mdrun -s tpr_NPT_anneal_240-240K.tpr -c gro_NPT_anneal_240-240K.gro -g log_NPT_anneal_240-240K.log -e edr_NPT_anneal_240-240K.edr -x xtc_NPT_anneal_240-240K.xtc -o trr_NPT_anneal_240-240K.trr

gmx grompp -f mdp_NPT_anneal_240-340K.mdp -c gro_NPT_anneal_240-240K.gro -p topol.top -o tpr_NPT_anneal_240-340K.tpr
gmx mdrun -s tpr_NPT_anneal_240-340K.tpr -c gro_NPT_anneal_240-340K.gro -g log_NPT_anneal_240-340K.log -e edr_NPT_anneal_240-340K.edr -x xtc_NPT_anneal_240-340K.xtc -o trr_NPT_anneal_240-340K.trr
