
task = 'phonons'

debug = False

lattice_vectors = [[ 2**(1/2),     0.00,     0.00], 
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','Cu','O','O','O','O',]
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.25,0.00],
                  [0.75,0.75,0.00]]

atom_files = ['Cu.py','O.py']

temperature = 0.01

spring_constants_file = 'spring_constants.py'
qpts_option = 'mesh'
qpts_mesh = [1,1,1]

phonon_output_file = 'phonons.hdf5'

