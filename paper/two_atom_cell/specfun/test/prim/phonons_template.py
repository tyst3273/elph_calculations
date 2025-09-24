
debug = False

task = 'phonons' 
temperature = 0.001

atom_files = ['Cu.py','O.py']
lattice_vectors = [[     1.00,     0.00,     0.00],
                   [     0.00,     1.00,     0.00],
                   [     0.00,     0.00,    10.00]]
atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]

spring_constants_file = 'spring_constants.py'

num_qpts_procs = 10
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 0.113/2,   0],
             [   0,   1,   0],
             [   0.78,   0,   0]]
# qpts_path = [[   0,   0,   0],
#              [-1/2, 1/2,   0]]
qpts_steps = 50

use_qpts_symmetry = False

phonon_output_file = 'phonons.hdf5'

_plot_phonon_bands = True







