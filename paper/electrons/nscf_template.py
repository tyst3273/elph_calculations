
debug = False

atom_files = ['Cu.py','O.py']
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

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [400,400,1]

num_kpts_procs = 8

use_hubbard_U = True
use_spin = True

do_electron_scf = False

temperature = 0.001

write_electron_eigenvectors = False

electron_delta_width = 0.015
calc_electron_fermi_surface = True

