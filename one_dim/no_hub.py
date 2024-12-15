#debug = True

task = 'nesting'
temperature = 0.001

num_electrons = 1
#electron_delta_width = 0.05

use_spin = False
num_electrons = 1
atom_files = ['Cu.py']
lattice_vectors = [[  1.00,  0.00,  0.00],
                   [  0.00, 10.00,  0.00],
                   [  0.00,  0.00, 10.00]]
atom_types = ['Cu']
atom_positions = [ 0.00, 0.00, 0.00]

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [100,1,1]
num_kpts_procs = 4

hopping_file = 'hopping.py'

do_electron_scf = False

electron_output_file = 'mesh.hdf5'

#num_qpts_procs = 4

#qpts_option = 'mesh'
#qpts_mesh = [100,1,1]
#use_qpts_symmetry = True

_plot_electron_bands = True

#qpts_option = 'user'
#qpts_user = [0.5,0.5,0]


