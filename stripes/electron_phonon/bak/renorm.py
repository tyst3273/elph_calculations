# linewidths converged-ish for phonon_self_energy_width = 0.01, kpts_mesh = [250,250,1]
# spectral function converged-ish for phonon_self_energy_eps = 0.0075 and kpts_mesh = [400,400,1]
# but doing coarse grid now for faster calcs

#debug = True

task = 'phonon_self_energy' #'phonon_line_widths'
temperature = 0.001

use_spin = True
use_hubbard_U = True

orbital_type = 'tight_binding'

site_density_input_file = 'nscf.hdf5'

kpts_option = 'mesh'
#kpts_mesh = [100,100,1] 
kpts_mesh = [40,20,1] 
num_kpts_procs = 1

hopping_file = 'hopping.py'
electron_fixed_fermi_energy = True

num_qpts_procs = 4
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0],
             [ 1/2,   0,   0],
             [   0,   0,   0]]
qpts_steps = 20

spring_constants_file = 'spring_constants.py'

### --- electron phonon ---

elph_output_file = 'renormalization.hdf5' #'full.hdf5'

phonon_self_energy_step = None 
phonon_self_energy_eps = 0.1 



atom_types = ['Cu','O','O','Cu','O','O','Cu','O','O','Cu','O','O','Cu','O','O','Cu','O','O','Cu','O',
	 'O','Cu','O','O']
spin_up_site_density = [  2.000,  0.000,  0.000,  0.000,  0.000,
			   0.000,  0.000,  0.000,  0.000,  0.000,
			   0.000,  0.000,  0.000,  0.000,  0.000,
			   0.000,  0.000,  0.000,  2.000,  0.000,
			   0.000,  0.000,  0.000,  0.000]
spin_down_site_density = [  0.000,  0.000,  0.000,  0.000,  0.000,
			   0.000,  2.000,  0.000,  0.000,  0.000,
			   0.000,  0.000,  2.000,  0.000,  0.000,
			   0.000,  0.000,  0.000,  0.000,  0.000,
			   0.000,  0.000,  0.000,  0.000]
atom_positions =  [[  0.000000,  0.000000,  0.000000],
	[  0.125000,  0.000000,  0.000000],
	[  0.000000,  0.250000,  0.000000],
	[  0.250000,  0.000000,  0.000000],
	[  0.375000,  0.000000,  0.000000],
	[  0.250000,  0.250000,  0.000000],
	[  0.500000,  0.000000,  0.000000],
	[  0.625000,  0.000000,  0.000000],
	[  0.500000,  0.250000,  0.000000],
	[  0.750000,  0.000000,  0.000000],
	[  0.875000,  0.000000,  0.000000],
	[  0.750000,  0.250000,  0.000000],
	[  0.000000,  0.500000,  0.000000],
	[  0.125000,  0.500000,  0.000000],
	[  0.000000,  0.750000,  0.000000],
	[  0.250000,  0.500000,  0.000000],
	[  0.375000,  0.500000,  0.000000],
	[  0.250000,  0.750000,  0.000000],
	[  0.500000,  0.500000,  0.000000],
	[  0.625000,  0.500000,  0.000000],
	[  0.500000,  0.750000,  0.000000],
	[  0.750000,  0.500000,  0.000000],
	[  0.875000,  0.500000,  0.000000],
	[  0.750000,  0.750000,  0.000000]]
lattice_vectors = [[  4.000000,  0.000000,  0.000000],
		   [  0.000000,  2.000000,  0.000000],
		   [  0.000000,  0.000000, 10.000000]]
num_electrons =   8.000