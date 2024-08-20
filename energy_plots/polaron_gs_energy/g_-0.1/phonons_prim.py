
debug = False

task = 'phonons'

temperature = 0.003
atom_files = ['Cu.py','O.py']

### --- phonons ---

spring_constants_file = 'spring_constants.py'

#qpts_option = 'mesh'
qpts_mesh = [200,200,1]
num_qpts_procs = 1

qpts_option = 'path'
qpts_path = [[0,0,0],[1/2,0,0],[1/2,1/2,0],[0,0,0]]
qpts_path = [[0,0,0],[1/2,1/2,0],[1,0,0],[0,0,0]] # matches primcell path
qpts_steps = 101
num_qpts_procs = 4

_plot_phonon_bands = True

phonon_output_file = 'phonons.hdf5'
write_phonon_eigenvectors = True

lattice_vectors = [[  1.00,  0.00,  0.00],
                   [  0.00,  1.00,  0.00],
                   [  0.00,  0.00, 10.00]]

atom_types = ['Cu','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.00,0.00],
                  [0.00,0.50,0.00]]

use_qpts_symmetry = True
#phonon_dos_step = 0.0001
phonon_dos_width = 0.005

