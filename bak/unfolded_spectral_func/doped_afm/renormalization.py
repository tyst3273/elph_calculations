# linewidths converged-ish for phonon_self_energy_width = 0.01, kpts_mesh = [250,250,1]
# spectral function converged-ish for phonon_self_energy_eps = 0.0075 and kpts_mesh = [400,400,1]
# but doing coarse grid now for faster calcs

#debug = True

task = 'phonon_self_energy' #'phonon_line_widths'
temperature = 0.01

use_spin = True
use_hubbard_U = True

num_electrons = 1.8

atom_files = ['Cu.py','O.py']
lattice_vectors = [[ 2**(1/2),     0.00,     0.00],
                   [     0.00, 2**(1/2),     0.00],
                   [     0.00,     0.00,    10.00]]
atom_types = ['Cu','Cu','O','O','O','O']
atom_positions = [[0.00,0.00,0.00],
                  [0.50,0.50,0.00],
                  [0.25,0.25,0.00],
                  [0.75,0.25,0.00],
                  [0.25,0.75,0.00],
                  [0.75,0.75,0.00]]

orbital_type = 'tight_binding'

site_density_input_file = 'nscf.hdf5'
#site_density = [1,1,0,0,0]

kpts_option = 'mesh'
#kpts_mesh = [100,100,1] 
kpts_mesh = [100,100,1] 
num_kpts_procs = 1

hopping_file = 'hopping.py'
electron_fixed_fermi_energy = True

num_qpts_procs = 8
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0]]
qpts_steps = 51

spring_constants_file = 'spring_constants.py'

### --- electron phonon ---

elph_output_file = 'renormalization.hdf5' #'full.hdf5'

phonon_self_energy_step = 0.0005
phonon_self_energy_eps = 0.05



