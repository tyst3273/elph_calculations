task = 'electrons'
debug = True
atom_positions_file = None
lattice_vectors = [[ 16.0, 0.0, 0.0],
    [ 0.0, 10.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = './'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.0625, 0.0, 0.0],
    [ 0.125, 0.0, 0.0],
    [ 0.1875, 0.0, 0.0],
    [ 0.25, 0.0, 0.0],
    [ 0.3125, 0.0, 0.0],
    [ 0.375, 0.0, 0.0],
    [ 0.4375, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.5625, 0.0, 0.0],
    [ 0.625, 0.0, 0.0],
    [ 0.6875, 0.0, 0.0],
    [ 0.75, 0.0, 0.0],
    [ 0.8125, 0.0, 0.0],
    [ 0.875, 0.0, 0.0],
    [ 0.9375, 0.0, 0.0]]
temperature = 0.001
num_electrons = 14.545454545454545
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 250, 1, 1]
use_kpts_symmetry = False
num_kpts_procs = 4
use_hubbard_U = True
spin_up_site_density = [ 0.9090909090909091, 0.0, 0.9090909090909091, 0.0,
     0.9090909090909091, 0.0, 0.9090909090909091, 0.0, 0.9090909090909091, 0.0,
     0.9090909090909091, 0.0, 0.9090909090909091, 0.0, 0.9090909090909091, 0.0,
   ]
spin_down_site_density = [ 0.0, 0.9090909090909091, 0.0, 0.9090909090909091,
     0.0, 0.9090909090909091, 0.0, 0.9090909090909091, 0.0, 0.9090909090909091,
     0.0, 0.9090909090909091, 0.0, 0.9090909090909091, 0.0, 0.9090909090909091,
   ]
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 0.01
electron_scf_energy_tol = 0.001
calc_electron_fermi_surface = False
electron_dos_step = None
electron_mix_method = 'simple'
electron_mix_alpha = 0.6
electron_output_file = 'scf_n_16_h_0.0909.hdf5'
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
anneal_end_temperature = 0.0001
anneal_step_size = 0.5
_plot_electron_bands = False
_write_kpts = False