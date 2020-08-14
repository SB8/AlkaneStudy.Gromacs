# HPC dicts

apocrita_sdv = {
	'mdrun': 'mpirun -np ${NSLOTS} gmx mdrun',
	'header': 'Apocrita_header_2019-4_sdv.sh',
	'header_null': 'Apocrita_header_2019-4_sdv_err-null.sh',
	'grompp': 'mpirun -np 1 gmx grompp'
}


apocrita_nxv = {
	'mdrun': 'gmx mdrun',
	'header': 'Apocrita_header_2019-4_nxv.sh',
	'grompp': 'gmx grompp'
}

empty = {
	'mdrun': 'mpirun -np ${NSLOTS} gmx_mpi mdrun',
	'header': 'empty_header.sh',
	'grompp': 'gmx grompp'
}

iridis = {
	'mdrun': 'mpirun -np 80 gmx_mpi mdrun',
	'header': 'Iridis_header_2019-4.sh',
	'header_null': 'Iridis_header_2019-4_err-null.sh',
	'grompp': 'gmx_mpi grompp'
}

MMM_2016_3 = {
	'mdrun': 'gerun mdrun_mpi',
	'header': 'MMM_header_2016-3.sh',
	'header_null': 'MMM_header_2016-3_err-null.sh',
	'grompp': 'gmx grompp'
}

MMM_2019_3 = {
	'mdrun': 'gerun mdrun_mpi',
	'header': 'MMM_header_2019-3.sh',
	'header_null': 'MMM_header_2019-3_err-null.sh',
	'grompp': 'gmx grompp'
}