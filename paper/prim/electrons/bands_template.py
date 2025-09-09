
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

kpts_option = 'path'
kpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
kpts_steps = 51

num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

do_electron_scf = False

temperature = 0.001

write_electron_eigenvectors = False

electron_fixed_fermi_energy =  True


