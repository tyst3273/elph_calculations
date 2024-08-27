
task = 'polaron_mft'

debug = False

lattice_vectors = [[ 2**(1/2),     0.00,     0.00], 
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]

atom_types = ['Cu','Cu','O','O','O','O',]
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.25,0.00],
                  [0.75,0.75,0.00]]

atom_files = ['Cu.py','O.py']

hopping_file = 'hopping.py'

orbital_type = 'tight_binding'

#use_kpts_symmetry = True
kpts_option = 'mesh'
kpts_mesh = [400,400,1]

num_kpts_procs = 8

site_density_input_file = 'electrons_restart.hdf5'

electron_output_file = 'electrons_nscf.hdf5'

use_hubbard_U = True
use_spin = True

do_electron_scf = False #True
max_electron_scf_steps = 400

electron_scf_density_tol = 1e-6
electron_scf_energy_tol = 1e-6

temperature = 0.01

num_electrons = 1.4

electron_mix_method = 'pulay'
electron_mix_alpha = 0.4
electron_mix_beta = 0.4
electron_mix_history = 4
electron_mix_delay = 10

write_electron_eigenvectors = False

spring_constants_file = 'spring_constants.py'
qpts_option = 'mesh'
qpts_mesh = [1,1,1]

phonon_output_file = None
phonon_eigenvectors_input_file = 'phonons.hdf5'

do_polaron_scf = False #True
max_polaron_scf_steps = 100
polaron_scf_displacement_tol = 1e-8

displacement_mix_method = 'simple'
displacement_mix_alpha = 0.8

polaron_output_file = 'polaron_restart.hdf5'

electron_dos_step = 0.01
electron_delta_width = 0.05
_plot_electron_bands = True

#calc_fermi_surface = True

