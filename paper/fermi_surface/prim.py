
debug = False

lattice_vectors = [[     1.00,     0.00,     0.00], 
                   [     0.00,     1.00,     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu']
atom_positions = [0.00,0.00,0.00]
atom_files = ['Cu.py']

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [400,400,1]
num_kpts_procs = 8

#use_kpts_symmetry = True

use_hubbard_U = False
use_spin = True

do_electron_scf = False

temperature = 0.001

#num_electrons = 1.6

write_electron_eigenvectors = False


electron_delta_width = 0.01
calc_electron_fermi_surface = True


