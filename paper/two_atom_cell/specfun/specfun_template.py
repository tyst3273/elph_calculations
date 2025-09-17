
debug = True

task = 'phonon_self_energy' 
temperature = 0.001

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

use_hubbard_U = True
use_spin = True

kpts_option = 'mesh'
# kpts_mesh = [50,50,1]
kpts_mesh = [100,100,1]
num_kpts_procs = 2

hopping_file = 'hopping.py'
spring_constants_file = 'spring_constants.py'

num_qpts_procs = 12
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0],
             [   1,   0,   0],
             [   0,   0,   0]]
qpts_steps = 100

### --- electron phonon ---

phonon_self_energy_step = 0.00025
phonon_self_energy_eps = 0.2
phonon_spectral_function_eps = 0.0001


"""
description: energy window around FS for calculating electron phonon matrix elements and 
    integrating. if None, all bands are used. if one float, the window is e-fermi +- the value. 
    if two values, the window is [e-fermi - lo, e-fermi + hi].
type: float, list of floats, None
"""
elph_electron_energy_window = None #

"""
description: only calculate electron-phonon stuff for phonons with frequency in this range.
    currently only has an effect for phonon self-energy calculations.
    if None, all modes are used. if one float, the window is 0 to the value. 
    if two values, the window is [min, to max].
type: float, list of floats, None
"""
elph_phonon_frequency_window = [0.15,0.25]











