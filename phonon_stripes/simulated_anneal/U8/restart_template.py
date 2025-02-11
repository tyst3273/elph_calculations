
task = 'electrons'
debug = False
temperature = 0.001
use_spin = True

atom_files = [ 'Cu.py','O.py']

orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'

use_kpts_symmetry = False
num_kpts_procs = 8

use_hubbard_U = True

do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 1e-4
electron_scf_energy_tol = 1e-5

calc_electron_fermi_surface = False
electron_dos_step = None

electron_mix_method = 'simple'
electron_mix_alpha = 0.8

write_electron_eigenvectors = False
write_site_density = True

