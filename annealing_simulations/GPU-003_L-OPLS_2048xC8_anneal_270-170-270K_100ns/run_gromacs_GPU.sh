
gmx grompp -f mdp_NPT_anneal_270-170K.mdp -c 2048xC8-AA_12nsEq_L-OPLS.gro -p topol.top -o tpr_NPT_anneal_270-170K.tpr
gmx mdrun -s tpr_NPT_anneal_270-170K.tpr -c gro_NPT_anneal_270-170K.gro -g log_NPT_anneal_270-170K.log -e edr_NPT_anneal_270-170K.edr -x xtc_NPT_anneal_270-170K.xtc -o trr_NPT_anneal_270-170K.trr

gmx grompp -f mdp_NPT_anneal_170-270K.mdp -c gro_NPT_anneal_270-170K.gro -p topol.top -o tpr_NPT_anneal_170-270K.tpr
gmx mdrun -s tpr_NPT_anneal_170-270K.tpr -c gro_NPT_anneal_170-270K.gro -g log_NPT_anneal_170-270K.log -e edr_NPT_anneal_170-270K.edr -x xtc_NPT_anneal_170-270K.xtc -o trr_NPT_anneal_170-270K.trr
