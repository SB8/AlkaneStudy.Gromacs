
gmx grompp -f mdp_NPT_anneal_340-240-340K_1.mdp -c 1024xC16_2nsEq-L-OPLS.gro -p topol.top -o tpr_NPT_anneal_340-240-340K_1.tpr
gmx mdrun -s tpr_NPT_anneal_340-240-340K_1.tpr -c gro_NPT_anneal_340-240-340K_1.gro -g log_NPT_anneal_340-240-340K_1.log -e edr_NPT_anneal_340-240-340K_1.edr -x xtc_NPT_anneal_340-240-340K_1.xtc 
