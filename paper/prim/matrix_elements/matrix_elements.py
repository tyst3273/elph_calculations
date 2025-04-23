# linewidths converged-ish for phonon_self_energy_width = 0.01, kpts_mesh = [250,250,1]
# spectral function converged-ish for phonon_self_energy_eps = 0.0075 and kpts_mesh = [400,400,1]
# but doing coarse grid now for faster calcs

#debug = True

task = 'elph_matrix_elements' #'phonon_line_widths'
temperature = 0.001

use_spin = True
num_electrons = 1
atom_files = ['Cu.py', 'O.py']
lattice_vectors = [[  1.00,  0.00,  0.00],
                   [  0.00,  1.00,  0.00],
                   [  0.00,  0.00, 10.00]]
atom_types = ['Cu', 'O', 'O']
atom_positions = [[ 0.00, 0.00, 0.00],
                  [ 0.50, 0.00, 0.00],
                  [ 0.00, 0.50, 0.00]]

orbital_type = 'tight_binding'

site_density = [1,0,0]
#spin_up_site_density = [1,0,0]
#spin_down_site_density = [0,0,0]

kpts_option = 'mesh'
#kpts_mesh = [400,400,1] 
kpts_mesh = [1,1,1]
num_kpts_procs = 4

hopping_file = 'hopping.py'
electron_fixed_fermi_energy = 0.0

num_qpts_procs = 6
qpts_option = 'path'
qpts_path = [[   0,   0,  0],
             [   0, 1/2,  0],
             [ 1/2, 1/2,  0],
             [   0,   0,  0]]
qpts_steps = 101

#qpts_option = 'user'
#qpts_user = [0.5,0.5,0]

spring_constants_file = 'spring_constants.py'

### --- electron phonon ---

elph_output_file = 'matrix_elements.hdf5'

#phonon_self_energy_do_adiabatic = True
#phonon_self_energy_do_non_adiabatic = True #True

#elph_phonon_frequency_window = [0.4,1.0]
#elph_electron_energy_window = None #2.0

#phonon_self_energy_step = 0.001
#phonon_self_energy_eps = 0.0075
#phonon_self_energy_eps = 0.01




