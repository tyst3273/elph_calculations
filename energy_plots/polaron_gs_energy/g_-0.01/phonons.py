
debug = False

task = 'phonons'

temperature = 0.003
atom_files = ['Cu.py','O.py']

### --- phonons ---

spring_constants_file = 'spring_constants.py'

qpts_option = 'mesh'
qpts_mesh = [1,1,1]
num_qpts_procs = 1

#qpts_option = 'path'
qpts_path = [[0,0,0],[1/2,0,0],[1/2,1/2,0],[0,0,0]]
qpts_path = [[0,0,0],[1/2,1/2,0],[1,0,0],[0,0,0]] # matches primcell path
qpts_steps = 101
num_qpts_procs = 4

#phonon_dos_step = 0.001
#phonon_dos_width = 0.01
_plot_phonon_bands = True

phonon_output_file = 'phonons.hdf5'
write_phonon_eigenvectors = True

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

atom_types = [ 'Cu', 'Cu', 'O', 'O', 'O', 'O']


use_qpts_symmetry = True
phonon_dos_step = 0.0001
phonon_dos_width = 0.005

