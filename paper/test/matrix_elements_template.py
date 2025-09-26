
debug = False

task = 'elph_matrix_elements' 
temperature = 0.001

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

orbital_type = 'tight_binding'

use_hubbard_U = True
use_spin = True

kpts_option = 'mesh'
# kpts_mesh = [50,50,1]
kpts_mesh = [10,10,1]
num_kpts_procs = 6

hopping_file = 'hopping.py'
spring_constants_file = 'spring_constants.py'

qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   1,   0],
             [   0,   0,   0]]
# qpts_path = [[-1/2,-1/2,   0],
#              [   0,   0,   0],
#              [ 1/2, 1/2,   0]]
qpts_steps = 51

use_qpts_symmetry = False

site_density_input_file = 'nscf.hdf5'

electron_fixed_fermi_energy = True
do_electron_scf = False

### --- electron phonon ---

num_electrons = 2.0

elph_output_file = 'matelem.hdf5'










