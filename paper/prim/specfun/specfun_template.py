
debug = False

task = 'phonon_self_energy' 
temperature = 0.001

atom_files = ['Cu.py', 'O.py']
lattice_vectors = [[  1.00,  0.00,  0.00],
                   [  0.00,  1.00,  0.00],
                   [  0.00,  0.00, 10.00]]
atom_types = ['Cu', 'O', 'O']
atom_positions = [[ 0.00, 0.00, 0.00],
                  [ 0.50, 0.00, 0.00],
                  [ 0.00, 0.50, 0.00]]

orbital_type = 'tight_binding'

use_hubbard_U = True
use_spin = True

kpts_option = 'mesh'
kpts_mesh = [100,100,1]
num_kpts_procs = 2

hopping_file = 'hopping.py'
spring_constants_file = 'spring_constants.py'

num_qpts_procs = 12
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/2, 1/2,   0],
             [   0,   0,   0]]
qpts_steps = 100

num_electrons = 1.0
# electron_fixed_fermi_energy = True
site_density_input_file = '../electrons/nscf/pm_U_0.00_N_1.00.hdf5'


### --- electron phonon ---

elph_output_file = 'specfun.hdf5'

phonon_self_energy_step = 0.00025
phonon_self_energy_eps = 0.2
phonon_spectral_function_eps = 0.0001








