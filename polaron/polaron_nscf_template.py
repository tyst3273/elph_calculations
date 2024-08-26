
### --- general ---

#debug = True

task = 'polaron_mft'

temperature = 0.001

atom_files = ['Cu.py','O.py']

### --- electrons ---

orbital_type = 'tight_binding'

use_hubbard_U = True
use_spin = True

hopping_file = 'hopping.py'

kpts_option = 'mesh'
kpts_mesh = [200,200,1]
num_kpts_procs = 4

electron_output_file = 'polaron_electrons.hdf5'
write_electron_eigenvectors = False
write_site_density = True

site_density_input_file = 'polaron_electrons.hdf5'

#electron_dos_step = 0.01
electron_delta_width = 0.001
#_plot_electron_bands = False

calc_electron_fermi_surface = True

do_electron_scf = False
max_electron_scf_steps = 100
electron_scf_energy_tol = 1e-4
electron_scf_density_tol = 1e-4

electron_mix_method = 'pulay'
electron_mix_alpha = 0.4
electron_mix_beta = 0.4
electron_mix_delay = 10
electron_mix_history = 4

### --- phonons ---

spring_constants_file = 'spring_constants.py'
qpts_option = 'mesh'
qpts_mesh = [1,1,1]

phonon_output_file = None

phonon_eigenvectors_input_file = 'phonons.hdf5'

### --- polaron ---

do_polaron_scf = False
max_polaron_scf_steps = 100
polaron_scf_displacement_tol = 1e-6

displacement_mix_method = 'simple'
displacement_mix_alpha = 0.8

polaron_output_file = 'polaron.hdf5'


