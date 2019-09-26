
gmx grompp -f mdp_NPT_anneal_340-240K.mdp -c 1024xC16-AA_2nsEq-L-OPLS.gro -p topol_CTL-HAL.top -o tpr_NPT_anneal_340-240K.tpr
gmx mdrun -s tpr_NPT_anneal_340-240K.tpr  -c gro_NPT_anneal_340-240K.gro -g log_NPT_anneal_340-240K.log -e edr_NPT_anneal_340-240K.edr -x xtc_NPT_anneal_340-240K.xtc

gmx grompp -f mdp_NPT_anneal_240-340K.mdp -c gro_NPT_anneal_340-240K.gro -p topol_CTL-HAL.top -o tpr_NPT_anneal_240-340K.tpr
gmx mdrun -s tpr_NPT_anneal_240-340K.tpr  -c gro_NPT_anneal_240-340K.gro -g log_NPT_anneal_240-340K.log -e edr_NPT_anneal_240-340K.edr -x xtc_NPT_anneal_240-340K.xtc
