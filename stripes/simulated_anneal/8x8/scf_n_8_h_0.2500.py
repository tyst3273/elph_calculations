task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 8.0, 0.0, 0.0],
    [ 0.0, 8.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = '/Users/ty/research/repos/elph_calculations/stripes/simulated_anneal/8x8'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.125, 0.0, 0.0],
    [ 0.25, 0.0, 0.0],
    [ 0.375, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.625, 0.0, 0.0],
    [ 0.75, 0.0, 0.0],
    [ 0.875, 0.0, 0.0],
    [ 0.0, 0.125, 0.0],
    [ 0.125, 0.125, 0.0],
    [ 0.25, 0.125, 0.0],
    [ 0.375, 0.125, 0.0],
    [ 0.5, 0.125, 0.0],
    [ 0.625, 0.125, 0.0],
    [ 0.75, 0.125, 0.0],
    [ 0.875, 0.125, 0.0],
    [ 0.0, 0.25, 0.0],
    [ 0.125, 0.25, 0.0],
    [ 0.25, 0.25, 0.0],
    [ 0.375, 0.25, 0.0],
    [ 0.5, 0.25, 0.0],
    [ 0.625, 0.25, 0.0],
    [ 0.75, 0.25, 0.0],
    [ 0.875, 0.25, 0.0],
    [ 0.0, 0.375, 0.0],
    [ 0.125, 0.375, 0.0],
    [ 0.25, 0.375, 0.0],
    [ 0.375, 0.375, 0.0],
    [ 0.5, 0.375, 0.0],
    [ 0.625, 0.375, 0.0],
    [ 0.75, 0.375, 0.0],
    [ 0.875, 0.375, 0.0],
    [ 0.0, 0.5, 0.0],
    [ 0.125, 0.5, 0.0],
    [ 0.25, 0.5, 0.0],
    [ 0.375, 0.5, 0.0],
    [ 0.5, 0.5, 0.0],
    [ 0.625, 0.5, 0.0],
    [ 0.75, 0.5, 0.0],
    [ 0.875, 0.5, 0.0],
    [ 0.0, 0.625, 0.0],
    [ 0.125, 0.625, 0.0],
    [ 0.25, 0.625, 0.0],
    [ 0.375, 0.625, 0.0],
    [ 0.5, 0.625, 0.0],
    [ 0.625, 0.625, 0.0],
    [ 0.75, 0.625, 0.0],
    [ 0.875, 0.625, 0.0],
    [ 0.0, 0.75, 0.0],
    [ 0.125, 0.75, 0.0],
    [ 0.25, 0.75, 0.0],
    [ 0.375, 0.75, 0.0],
    [ 0.5, 0.75, 0.0],
    [ 0.625, 0.75, 0.0],
    [ 0.75, 0.75, 0.0],
    [ 0.875, 0.75, 0.0],
    [ 0.0, 0.875, 0.0],
    [ 0.125, 0.875, 0.0],
    [ 0.25, 0.875, 0.0],
    [ 0.375, 0.875, 0.0],
    [ 0.5, 0.875, 0.0],
    [ 0.625, 0.875, 0.0],
    [ 0.75, 0.875, 0.0],
    [ 0.875, 0.875, 0.0]]
temperature = 0.001
num_electrons = 48.0
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 10, 10, 1]
use_kpts_symmetry = False
num_kpts_procs = 6
use_hubbard_U = True
spin_up_site_density = [ 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.0,
     0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0,
     0.75, 0.0, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.75, 0.0, 0.75,
     0.0, 0.75, 0.0, 0.75, 0.0, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.75,
     0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0,
     0.75]
spin_down_site_density = [ 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.75,
     0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0,
     0.75, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.0, 0.75, 0.0, 0.75,
     0.0, 0.75, 0.0, 0.75, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.0, 0.75,
     0.0, 0.75, 0.0, 0.75, 0.0, 0.75, 0.75, 0.0, 0.75, 0.0, 0.75, 0.0, 0.75,
     0.0]
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 0.001
electron_scf_energy_tol = 1e-05
calc_electron_fermi_surface = False
electron_dos_step = None
electron_mix_method = 'simple'
electron_mix_alpha = 0.8
electron_output_file = 'scf_n_8_h_0.2500.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = None
job_description = None
write_kpts_hdf5_file = False
do_simulated_annealing = True
num_anneal_steps = 50
max_anneal_steps = 75
anneal_start_temperature = 0.1
anneal_end_temperature = 0.001
anneal_step_size = 0.5
_plot_electron_bands = False
_write_kpts = False
