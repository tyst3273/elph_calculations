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
kpts_mesh = [ 4, 4, 1]
use_kpts_symmetry = False
num_kpts_procs = 4
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
electron_eigenvectors_input_file = None
job_description = None
_plot_electron_bands = False
_write_kpts = False