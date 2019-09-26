
gmx grompp -f mdp_NPT_sim.mdp -c 1024xC16-AA_2nsEq.gro -p topol.top -o tpr_NPT_sim.tpr
gmx mdrun -s tpr_NPT_sim.tpr -c gro_NPT_sim.gro -g log_NPT_sim.log -e edr_NPT_sim.edr -x xtc_NPT_sim.xtc 
