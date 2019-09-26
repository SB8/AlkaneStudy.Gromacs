
gmx grompp -f mdp_NPT_anneal_220-160K.mdp -c 2048xC8-AA_5nsEq-CHARMM36.gro -p topol.top -o tpr_NPT_anneal_220-160K.tpr
gmx mdrun -s tpr_NPT_anneal_220-160K.tpr -c gro_NPT_anneal_220-160K.gro -g log_NPT_anneal_220-160K.log -e edr_NPT_anneal_220-160K.edr -x xtc_NPT_anneal_220-160K.xtc

gmx grompp -f mdp_NPT_anneal_160-220K.mdp -c gro_NPT_anneal_220-160K.gro -p topol.top -o tpr_NPT_anneal_160-220K.tpr
gmx mdrun -s tpr_NPT_anneal_160-220K.tpr -c gro_NPT_anneal_160-220K.gro -g log_NPT_anneal_160-220K.log -e edr_NPT_anneal_160-220K.edr -x xtc_NPT_anneal_160-220K.xtc
