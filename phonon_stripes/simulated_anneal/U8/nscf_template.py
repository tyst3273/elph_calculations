
task = 'electrons'
debug = False
atom_files = [ 'Cu.py','O.py']

temperature = 0.001

use_spin = True
orbital_type = 'tight_binding'
hopping_file = 'hopping.py'
kpts_option = 'mesh'


use_kpts_symmetry = False
num_kpts_procs = 8

use_hubbard_U = True

do_electron_scf = False

write_electron_eigenvectors = False
write_site_density = True

electron_dos_step = 0.01
electron_delta_width = 0.025
calc_electron_fermi_surface = True
