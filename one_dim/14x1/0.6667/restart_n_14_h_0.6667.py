task = 'electrons'
debug = False
atom_positions_file = None
lattice_vectors = [[ 14.0, 0.0, 0.0],
    [ 0.0, 10.0, 0.0],
    [ 0.0, 0.0, 10.0]]
atom_types = [ 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu',
     'Cu', 'Cu', 'Cu', 'Cu']
atom_files = [ 'Cu.py']
atom_files_dir = './'
atom_positions = [[ 0.0, 0.0, 0.0],
    [ 0.07142857142857142, 0.0, 0.0],
    [ 0.14285714285714285, 0.0, 0.0],
    [ 0.21428571428571427, 0.0, 0.0],
    [ 0.2857142857142857, 0.0, 0.0],
    [ 0.35714285714285715, 0.0, 0.0],
    [ 0.42857142857142855, 0.0, 0.0],
    [ 0.5, 0.0, 0.0],
    [ 0.5714285714285714, 0.0, 0.0],
    [ 0.6428571428571429, 0.0, 0.0],
    [ 0.7142857142857143, 0.0, 0.0],
    [ 0.7857142857142857, 0.0, 0.0],
    [ 0.8571428571428571, 0.0, 0.0],
    [ 0.9285714285714286, 0.0, 0.0]]
temperature = 0.001
num_electrons = 4.666666666666667
num_bands = None
use_spin = True
orbital_type = 'tight_binding'
potential_type = None
hopping_file = 'hopping.py'
kpts_option = 'mesh'
kpts_mesh = [ 268, 1, 1]
use_kpts_symmetry = False
num_kpts_procs = 4
use_hubbard_U = True
spin_up_site_density = [ 0.33333333333333337, 0.0, 0.33333333333333337, 0.0,
     0.33333333333333337, 0.0, 0.33333333333333337, 0.0, 0.33333333333333337,
     0.0, 0.33333333333333337, 0.0, 0.33333333333333337, 0.0]
spin_down_site_density = [ 0.0, 0.33333333333333337, 0.0, 0.33333333333333337,
     0.0, 0.33333333333333337, 0.0, 0.33333333333333337, 0.0, 0.33333333333333337,
     0.0, 0.33333333333333337, 0.0, 0.33333333333333337]
do_electron_scf = True
max_electron_scf_steps = 100
electron_scf_density_tol = 0.0001
electron_scf_energy_tol = 1e-05
calc_electron_fermi_surface = False
electron_dos_step = None
electron_mix_method = 'simple'
electron_mix_alpha = 0.8
electron_output_file = 'restart_n_14_h_0.6667.hdf5'
write_electron_eigenvectors = False
write_site_density = True
electron_eigenvectors_input_file = None
site_density_input_file = 'scf_n_14_h_0.6667.hdf5'
job_description = None
write_kpts_hdf5_file = False
do_simulated_annealing = False
_plot_electron_bands = False
_write_kpts = False
