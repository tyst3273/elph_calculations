
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np
import os
import time

# --------------------------------------------------------------------------------------------------

input_file = 'bands_template.py'

kpts_path = [[   0,   0,   0],
             [ 1/2, 1/2,   0]]
kwargs = {'electron_output_file' : f'k1.hdf5',
          'kpts_path' : kpts_path}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kpts_path = [[   0,   0,   0],
             [-1/2, 1/2,   0]]
kwargs = {'electron_output_file' : f'k2.hdf5',
          'kpts_path' : kpts_path}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kpts_path = [[   0,   0,   0],
             [ 1/2,-1/2,   0]]
kwargs = {'electron_output_file' : f'k3.hdf5',
          'kpts_path' : kpts_path}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

kpts_path = [[   0,   0,   0],
             [-1/2,-1/2,   0]]
kwargs = {'electron_output_file' : f'k4.hdf5',
          'kpts_path' : kpts_path}
ELPH = c_ELPH(input_file)
ELPH.set_config(**kwargs)
ELPH.run()

# --------------------------------------------------------------------------------------------------



