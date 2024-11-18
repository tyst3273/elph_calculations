
debug = False

task = 'electrons'
temperature = 0.001

atom_files = ['Cu.py','O.py']

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [200,400,1]
num_kpts_procs = 16

use_hubbard_U = True
use_spin = True

do_electron_scf = False

electron_mix_method = 'pulay'
electron_mix_alpha = 0.6
electron_mix_beta = 0.2
electron_mix_delay = 10
electron_mix_history = 4

site_density_input_file = 'density.hdf5'
electron_output_file = 'nscf.hdf5'
write_electron_eigenvectors = False

_plot_electron_bands = True

electron_delta_width = 0.01
calc_electron_fermi_surface = True



