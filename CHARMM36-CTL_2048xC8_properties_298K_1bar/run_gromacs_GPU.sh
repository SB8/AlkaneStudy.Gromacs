
gmx grompp -f mdp_EM.mdp -c 2048xC8_AA_start.gro -p topol.top -o tpr_EM.tpr
gerun mdrun_mpi -s tpr_EM.tpr  -c gro_EM.gro -g log_EM.log -e edr_EM.edr -o trr_EM.trr

gmx grompp -f mdp_NPT_eq.mdp -c gro_EM.gro -p topol.top -o tpr_NPT_eq.tpr
gerun mdrun_mpi -s tpr_NPT_eq.tpr  -c gro_NPT_eq.gro -g log_NPT_eq.log -e edr_NPT_eq.edr -x xtc_NPT_eq.xtc

gmx grompp -f mdp_NPT_sim.mdp -c gro_NPT_eq.gro -p topol.top -o tpr_NPT_sim.tpr
gerun mdrun_mpi -s tpr_NPT_sim.tpr  -c gro_NPT_sim.gro -g log_NPT_sim.log -e edr_NPT_sim.edr -x xtc_NPT_sim.xtc

sleep 1
python3 box_resize.py gmx gro_NPT_sim.gro 3 gro_interface_start.gro
sleep 1

gmx grompp -f mdp_NVT_interface.mdp -c gro_interface_start.gro -p topol.top -o tpr_NVT_interface.tpr
gerun mdrun_mpi -s tpr_NVT_interface.tpr  -c gro_NVT_interface.gro -g log_NVT_interface.log -e edr_NVT_interface.edr -x xtc_NVT_interface.xtc
