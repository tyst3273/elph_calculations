
debug = False

task = 'electrons'
temperature = 0.01

hopping_file = 'hopping.py'
orbital_type = 'tight_binding'

kpts_option = 'mesh'
kpts_mesh = [10,10,1]
num_kpts_procs = 4

use_hubbard_U = True
use_spin = True

do_electron_scf = True

max_electron_scf_steps = 400
electron_scf_density_tol = 1e-4
electron_scf_energy_tol = 1e-4

electron_mix_method = 'pulay'
electron_mix_alpha = 0.6
electron_mix_beta = 0.2
electron_mix_delay = 10
electron_mix_history = 4

write_electron_eigenvectors = False
write_site_density = True


