
debug = False

task = 'electrons'
temperature = 0.01

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [400,400,1]
num_kpts_procs = 4

do_electron_scf = False

write_electron_eigenvectors = False
write_site_density = True

electron_delta_width = 0.05
calc_electron_fermi_surface = True

use_spin = True
num_electrons = 1
atom_files = ['Cu.py', 'O.py']
lattice_vectors = [[  1.00,  0.00,  0.00],
                   [  0.00,  1.00,  0.00],
                   [  0.00,  0.00, 10.00]]
atom_types = ['Cu', 'O', 'O']
atom_positions = [[ 0.00, 0.00, 0.00],
                  [ 0.50, 0.00, 0.00],
                  [ 0.00, 0.50, 0.00]]

