
gmx grompp -f mdp_NPT_anneal_330-230K.mdp -c 1024xC15-AA_12nsEq_L-OPLS.gro -p topol.top -o tpr_NPT_anneal_330-230K.tpr
gmx mdrun -s tpr_NPT_anneal_330-230K.tpr -c gro_NPT_anneal_330-230K.gro -g log_NPT_anneal_330-230K.log -e edr_NPT_anneal_330-230K.edr -x xtc_NPT_anneal_330-230K.xtc -o trr_NPT_anneal_330-230K.trr

gmx grompp -f mdp_NPT_anneal_230-330K.mdp -c gro_NPT_anneal_330-230K.gro -p topol.top -o tpr_NPT_anneal_230-330K.tpr
gmx mdrun -s tpr_NPT_anneal_230-330K.tpr -c gro_NPT_anneal_230-330K.gro -g log_NPT_anneal_230-330K.log -e edr_NPT_anneal_230-330K.edr -x xtc_NPT_anneal_230-330K.xtc -o trr_NPT_anneal_230-330K.trr
