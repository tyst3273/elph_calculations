
debug = False

lattice_vectors = [[ 2**(1/2),     0.00,     0.00], 
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','Cu']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00]]

atom_files = ['Cu.py']

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [400,400,1]

num_kpts_procs = 10

use_hubbard_U = True
use_spin = True

do_electron_scf = False
max_electron_scf_steps = 400

temperature = 0.001

write_electron_eigenvectors = False

