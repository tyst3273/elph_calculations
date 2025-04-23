
debug = False

atom_files = ['Cu.py','O.py']
lattice_vectors = [[ 1.00,     0.00,     0.00],
                   [ 0.00,     1.00,     0.00],
                   [ 0.00,     0.00,    10.00]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.50,0.50,0.00]]

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [400,400,1]

num_kpts_procs = 8

use_hubbard_U = False
use_spin = True

do_electron_scf = True
max_electron_scf_steps = 400

electron_scf_density_tol = 1e-4
electron_scf_energy_tol = 1e-5

temperature = 0.001

electron_mix_method = 'pulay'
electron_mix_alpha = 0.4
electron_mix_beta = 0.4
electron_mix_history = 4
electron_mix_delay = 10

write_electron_eigenvectors = False

num_electrons = 1.0

electron_delta_width = 0.01
calc_electron_fermi_surface = True

electron_dos_step = 0.01

_plot_electron_bands = True

