
debug = False

task = 'nesting'

atom_files = ['Cu.py']
lattice_vectors = [[ 1.00,     0.00,     0.00],
                   [ 0.00,     1.00,     0.00],
                   [ 0.00,     0.00,    10.00]]
atom_types = ['Cu']
atom_positions = [[0.00,0.00,0.00]]

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [200,200,1]

num_kpts_procs = 4

use_hubbard_U = False
use_spin = False

do_electron_scf = False
max_electron_scf_steps = 400

temperature = 0.001
write_electron_eigenvectors = False


qpts_mesh = [100,100,1]
use_qpts_symmetry = True

electron_delta_width = 0.05