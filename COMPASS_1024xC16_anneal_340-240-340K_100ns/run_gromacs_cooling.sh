
gmx grompp -f mdp_NPT_anneal_340-240K.mdp -c 1024xC16_2nsEq-L-OPLS.gro -p topol.top -o tpr_NPT_anneal_340-240K.tpr
gerun mdrun_mpi -s tpr_NPT_anneal_340-240K.tpr -c gro_NPT_anneal_340-240K.gro -g log_NPT_anneal_340-240K.log -e edr_NPT_anneal_340-240K.edr -x xtc_NPT_anneal_340-240K.xtc 
