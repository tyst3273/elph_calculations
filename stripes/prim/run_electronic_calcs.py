
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt
import os

# template to get args from
nscf_template = 'nscf_template.py'

num_elec = np.arange(0.05,1.95,0.05)

# loop over fillings 
num_calcs = num_elec.size
for ii, n in enumerate(num_elec):
    
    n = num_elec[ii]
    nscf_output_file = f'nscf_n_{n:.2f}.hdf5'

    # run nscf cal
    kwargs = {'electron_output_file':nscf_output_file,
              'num_electrons':n}
    ELPH = c_ELPH(nscf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()


