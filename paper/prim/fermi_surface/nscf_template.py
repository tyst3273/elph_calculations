
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
use_spin = False

do_electron_scf = False
max_electron_scf_steps = 400

temperature = 0.001
write_electron_eigenvectors = False

electron_delta_width = 0.025
calc_electron_fermi_surface = True
