
debug = False

task = 'elph_matrix_elements' 
temperature = 0.001

atom_files = ['Cu.py','O.py']
lattice_vectors = [[     1.00,     0.00,     0.00],
                   [     0.00,     1.00,     0.00],
                   [     0.00,     0.00,    10.00]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]
spin_up_site_density = [1, 0, 0]
spin_down_site_density = [1, 0, 0]

orbital_type = 'tight_binding'

use_hubbard_U = True
use_spin = True

kpts_option = 'mesh'
kpts_mesh = [50,50,1]
num_kpts_procs = 8

hopping_file = 'hopping.py'
spring_constants_file = 'spring_constants.py'

qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
# qpts_path = [[   0,   0,   0],
#              [ 1/2, 1/2,   0]]
qpts_steps = 25

use_qpts_symmetry = False

site_density_input_file = 'nscf.hdf5'

electron_fixed_fermi_energy = True
do_electron_scf = False

### --- electron phonon ---

elph_output_file = 'matelem_1.hdf5'










