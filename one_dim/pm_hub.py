#debug = True

task = 'nesting'
temperature = 0.001

num_electrons = 2
#electron_delta_width = 0.05

use_spin = False
atom_files = ['Cu.py']
lattice_vectors = [[  2.00,  0.00,  0.00],
                   [  0.00, 10.00,  0.00],
                   [  0.00,  0.00, 10.00]]
atom_types = ['Cu','Cu']
atom_positions = [ [0.00, 0.00, 0.00], [0.50, 0.00, 0.00]]

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [1000,1,1]
num_kpts_procs = 4

hopping_file = 'hopping.py'

use_hubbard_U = True
use_spin = True

do_electron_scf = True
electron_scf_energy_tol = 1e-6
electron_scf_density_tol = 1e-6

spin_up_site_density = [1,1]
spin_down_site_density = [1,1]

electron_output_file = 'mesh.hdf5'

#num_qpts_procs = 4

#qpts_option = 'mesh'
#qpts_mesh = [100,1,1]
#use_qpts_symmetry = True

_plot_electron_bands = True

#qpts_option = 'user'
#qpts_user = [0.5,0.5,0]


