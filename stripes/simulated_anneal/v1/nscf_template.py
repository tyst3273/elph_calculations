
#debug = True 

task = 'electrons'
temperature = 0.01

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [50,50,1]
num_kpts_procs = 4

use_hubbard_U = True
use_spin = True

do_electron_scf = False

write_electron_eigenvectors = False
write_site_density = True

atom_files = ['Cu.py']

electron_dos_step = 0.001
electron_delta_width = 0.05
_plot_electron_bands = True

