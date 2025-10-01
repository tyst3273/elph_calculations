
debug = True

task = 'phonons' 
temperature = 0.001

atom_files = ['A.py','B.py']
lattice_vectors = [[   1,          0,  0],
                   [ 1/2, 3**(1/2)/2,  0],
                   [   0,          0, 10] ]
atom_types = ['A','B']
atom_positions = [[0.000000, 0.000000, 0.000000],
                  [0.333333, 0.666667, 0.000000]]

spring_constants_file = 'spring_constants.py'

num_qpts_procs = 10
qpts_option = 'path'
qpts_path = [[   0,   0,   0],
             [ 1/2,   0,   0],
             [ 1/3, 1/3,   0]]
qpts_steps = 101

use_qpts_symmetry = True

phonon_output_file = 'phonons.hdf5'
_plot_phonon_bands = True

# Graphene
# 1.0
# 2.460000 0.000000 0.000000
# 1.230000 2.130422 0.000000
# 0.000000 0.000000 15.000000
# C
# 2
# Direct
# 0.000000 0.000000 0.500000
# 0.333333 0.666667 0.500000

# Γ = (0,0,0)
# M = (0.5, 0, 0)
# K = (1/3, 1/3, 0)






