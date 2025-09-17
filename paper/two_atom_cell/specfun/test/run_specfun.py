
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np
import os
import time

# --------------------------------------------------------------------------------------------------

input_file = 'specfun_template.py'

qpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0]]
kwargs = {'elph_output_file' : f'q1_new.hdf5',
          'qpts_path' : qpts_path}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

qpts_path = [[   0,   0,   0],
             [-1/2, 1/2,   0]]
kwargs = {'elph_output_file' : f'q2_new.hdf5',
          'qpts_path' : qpts_path}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

# qpts_path = [[   0,   0,   0],
#              [ 1/2,-1/2,   0]]
# kwargs = {'elph_output_file' : f'q3_new.hdf5',
#           'qpts_path' : qpts_path}
# ELPH = c_ELPH(input_file)
# ELPH.set_config(**kwargs)
# ELPH.run()

# qpts_path = [[   0,   0,   0],
#              [-1/2,-1/2,   0]]
# kwargs = {'elph_output_file' : f'q4_new.hdf5',
#           'qpts_path' : qpts_path}
# ELPH = c_ELPH(input_file)
# ELPH.set_config(**kwargs)
# ELPH.run()


# --------------------------------------------------------------------------------------------------



