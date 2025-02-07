task = 'phonons'
debug = False
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
qpts_option = 'mesh'
qpts_mesh = [ 1, 1, 1]
use_qpts_symmetry = False
num_qpts_procs = 4
spring_constants_file = 'spring_constants.py'
phonon_output_file = 'phonons_n_2.hdf5'
write_phonon_eigenvectors = True
phonon_eigenvectors_input_file = None
phonon_dos_step = None
job_description = None
write_qpts_hdf5_file = False
_plot_phonon_bands = False
_write_qpts = False
