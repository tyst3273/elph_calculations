
#debug = True

task = 'electrons'
temperature = 0.01

atom_positions = [0.5,0.5,0.0]
lattice_vectors = [[ 1.0,  0.0,  0.0],
                   [ 0.0,  1.0,  0.0],
                   [ 0.0,  0.0, 10.0]]
atom_types = ['Cu']
atom_files = ['Cu.py']

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [400,400,1]
num_kpts_procs = 4

use_spin = False
do_electron_scf = False

write_electron_eigenvectors = False

electron_delta_width = 0.05
calc_electron_fermi_surface = True

# dos
#electron_dos_step = 0.05
#_plot_electron_bands = True

