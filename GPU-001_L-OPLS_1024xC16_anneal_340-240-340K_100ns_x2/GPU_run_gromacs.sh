
gmx grompp -f mdp_EM.mdp -c 1024xC16-AA_start.gro -p topol.top -o tpr_EM.tpr
gmx mdrun -s tpr_EM.tpr -c gro_EM.gro -g log_EM.log -e edr_EM.edr -o trr_EM.trr 

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq.tpr
gmx mdrun -s tpr_NPT_eq.tpr -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc 

gmx grompp -f mdp_NPT_anneal_340-240-340K_cycle1.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_anneal_340-240-340K_cycle1.tpr
gmx mdrun -s tpr_NPT_anneal_340-240-340K_cycle1.tpr -c gro_NPT_anneal_340-240-340K_cycle1.gro -g log_NPT_anneal_340-240-340K_cycle1.log -e edr_NPT_anneal_340-240-340K_cycle1.edr -x xtc_NPT_anneal_340-240-340K_cycle1.xtc 

gmx grompp -f mdp_NPT_anneal_340-240-340K_cycle2.mdp -c gro_NPT_anneal_340-240-340K_cycle1.gro -p topol.top -o tpr_NPT_anneal_340-240-340K_cycle2.tpr
gmx mdrun -s tpr_NPT_anneal_340-240-340K_cycle2.tpr -c gro_NPT_anneal_340-240-340K_cycle2.gro -g log_NPT_anneal_340-240-340K_cycle2.log -e edr_NPT_anneal_340-240-340K_cycle2.edr -x xtc_NPT_anneal_340-240-340K_cycle2.xtc 
