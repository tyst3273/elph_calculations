task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 22.0, 0.0, 0.0],
    [ 0.0, 10.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
   ]
atom_files = [ 'Cu.py']
atom_files_dir = './'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.045454545454545456, 0.0, 0.0],
    [ 0.09090909090909091, 0.0, 0.0],
    [ 0.13636363636363635, 0.0, 0.0],
    [ 0.18181818181818182, 0.0, 0.0],
    [ 0.22727272727272727, 0.0, 0.0],
    [ 0.2727272727272727, 0.0, 0.0],
    [ 0.3181818181818182, 0.0, 0.0],
    [ 0.36363636363636365, 0.0, 0.0],
    [ 0.4090909090909091, 0.0, 0.0],
    [ 0.45454545454545453, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.5454545454545454, 0.0, 0.0],
    [ 0.5909090909090909, 0.0, 0.0],
    [ 0.6363636363636364, 0.0, 0.0],
    [ 0.6818181818181818, 0.0, 0.0],
    [ 0.7272727272727273, 0.0, 0.0],
    [ 0.7727272727272727, 0.0, 0.0],
    [ 0.8181818181818182, 0.0, 0.0],
    [ 0.8636363636363636, 0.0, 0.0],
    [ 0.9090909090909091, 0.0, 0.0],
    [ 0.9545454545454546, 0.0, 0.0]]
temperature = 0.001
num_electrons = 18.333333333333336
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 214, 1, 1]
use_kpts_symmetry = False
num_kpts_procs = 4
use_hubbard_U = True
spin_up_site_density = [ 0.8333333333333335, 0.0, 0.8333333333333335, 0.0,
     0.8333333333333335, 0.0, 0.8333333333333335, 0.0, 0.8333333333333335, 0.0,
     0.8333333333333335, 0.0, 0.8333333333333335, 0.0, 0.8333333333333335, 0.0,
     0.8333333333333335, 0.0, 0.8333333333333335, 0.0, 0.8333333333333335, 0.0,
   ]
spin_down_site_density = [ 0.0, 0.8333333333333335, 0.0, 0.8333333333333335,
     0.0, 0.8333333333333335, 0.0, 0.8333333333333335, 0.0, 0.8333333333333335,
     0.0, 0.8333333333333335, 0.0, 0.8333333333333335, 0.0, 0.8333333333333335,
     0.0, 0.8333333333333335, 0.0, 0.8333333333333335, 0.0, 0.8333333333333335,
   ]
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 0.0001
electron_scf_energy_tol = 1e-05
calc_electron_fermi_surface = False
electron_dos_step = None
electron_mix_method = 'simple'
electron_mix_alpha = 0.8
electron_output_file = 'restart_n_22_h_0.1667.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = 'scf_n_22_h_0.1667.hdf5'
job_description = None
write_kpts_hdf5_file = False
do_simulated_annealing = False
_plot_electron_bands = False
_write_kpts = False