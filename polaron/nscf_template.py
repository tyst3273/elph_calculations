
#debug = True

task = 'electrons'

temperature = 0.01

atom_files = ['Cu.py','O.py']

### --- electrons ---

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [200,200,1]
num_kpts_procs = 4

use_hubbard_U = True
use_spin = True

do_electron_scf = False

electron_output_file = 'nscf_density.hdf5'
site_density_input_file = 'scf_density.hdf5'
write_electron_eigenvectors = False
write_site_density = True

electron_dos_step = 0.01
electron_delta_width = 0.05
_plot_electron_bands = True


