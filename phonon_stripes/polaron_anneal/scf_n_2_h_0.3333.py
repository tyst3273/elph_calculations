task = 'polaron_mft'
debug = True
atom_positions_file = None
lattice_vectors = [[ 2.0, 0.0, 0.0],
    [ 0.0, 2.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O', 'O', 'Cu', 'O',
     'O']
atom_files = [ 'Cu.py', 'O.py']
atom_files_dir = '/home/ty/research/repos/elph_calculations/phonon_stripes/simulated_anneal'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.25, 0.0, 0.0],
    [ 0.0, 0.25, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.75, 0.0, 0.0],
    [ 0.5, 0.25, 0.0],
    [ 0.0, 0.5, 0.0],
    [ 0.25, 0.5, 0.0],
    [ 0.0, 0.75, 0.0],
    [ 0.5, 0.5, 0.0],
    [ 0.75, 0.5, 0.0],
    [ 0.5, 0.75, 0.0]]
temperature = 0.001
num_electrons = 2.666666666666667
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 250, 250, 1]
use_kpts_symmetry = False
num_kpts_procs = 8
use_hubbard_U = False
spin_up_site_density = [ 0.6666666666666667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.6666666666666667, 0.0, 0.0]
spin_down_site_density = [ 0.0, 0.0, 0.0, 0.6666666666666667, 0.0, 0.0, 0.6666666666666667,
     0.0, 0.0, 0.0, 0.0, 0.0]
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 0.0004
electron_scf_energy_tol = 4e-05
calc_electron_fermi_surface = False
electron_dos_step = None
electron_mix_method = 'simple'
electron_mix_alpha = 0.8
electron_output_file = 'scf_n_2_h_0.3333.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = None
qpts_option = 'mesh'
qpts_mesh = [ 1, 1, 1]
use_qpts_symmetry = False
num_qpts_procs = 1
spring_constants_file = 'spring_constants.py'
phonon_output_file = 'phonons_n_2.hdf5'
write_phonon_eigenvectors = True
phonon_eigenvectors_input_file = 'phonons_n_2.hdf5'
phonon_dos_step = None
polaron_output_file = 'polaron_out.hdf5'
do_polaron_scf = True
max_polaron_scf_steps = 100
polaron_scf_displacement_tol = 0.0004
displacement_mix_method = 'simple'
displacement_mix_alpha = 0.8
job_description = None
write_kpts_hdf5_file = False
write_qpts_hdf5_file = False
do_simulated_annealing = False
num_anneal_steps = 50
max_anneal_steps = 75
anneal_start_temperature = 1.0
anneal_end_temperature = 0.001
anneal_step_size = 0.1
do_polaron_simulated_annealing = True
_plot_electron_bands = False
_plot_phonon_bands = False
_write_qpts = False
_write_kpts = False
