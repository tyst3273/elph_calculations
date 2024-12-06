
#debug = True #False
#num_mkl_threads = 1

task = 'electrons'

temperature = 0.05

atom_files = ['Cu.py','O.py']
atom_files_dir = 'input'


### --- electrons ---

hopping_file = 'input/hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [150,150,1]
num_kpts_procs = 4

use_hubbard_U = False #True
use_spin = True

do_electron_scf = True
max_electron_scf_steps = 400
electron_scf_density_tol = 1e-9
electron_scf_energy_tol = 1e-6

electron_dos_step = 0.001
electron_dos_width = 0.1
_plot_electron_bands = True


electron_mix_method = 'pulay'
electron_mix_alpha = 0.4
electron_mix_beta = 0.2
electron_mix_delay = 10
electron_mix_history = 4

electron_output_file = 'density.hdf5'
write_electron_eigenvectors = False
write_site_density = True


num_electrons = 2

lattice_vectors = [[ 2**(1/2),     0.00,     0.00],
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','Cu','O','O','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.75,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.75,0.00]]

atom_types = [ 'Cu', 'Cu', 'O', 'O', 'O', 'O']

spin_up_site_density = [ 1, 1, 0,0,0,0] 
spin_down_site_density = [ 1, 1, 0,0,0,0]


