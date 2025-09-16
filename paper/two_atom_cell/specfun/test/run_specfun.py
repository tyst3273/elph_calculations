
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np
import os
import time

# --------------------------------------------------------------------------------------------------

input_file = 'specfun_template.py'

kwargs = {'elph_output_file' : f'nk_100_T_0.01.hdf5',
          'temperature' : 0.01}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kwargs = {'elph_output_file' : f'nk_100_T_0.001.hdf5',
          'temperature' : 0.001}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kwargs = {'elph_output_file' : f'nk_100_T_0.0001.hdf5',
          'temperature' : 0.0001}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kwargs = {'elph_output_file' : f'nk_100_T_0.00001.hdf5',
          'temperature' : 0.00001}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kwargs = {'elph_output_file' : f'nk_100_T_0.000001.hdf5',
          'temperature' : 0.000001}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

# --------------------------------------------------------------------------------------------------



