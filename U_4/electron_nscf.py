
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

#use_kpts_symmetry = True
kpts_option = 'mesh'
kpts_mesh = [400,400,1]
num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

do_electron_scf = False

temperature = 0.01

write_electron_eigenvectors = False

electron_dos_step = 0.01
electron_delta_width = 0.075

