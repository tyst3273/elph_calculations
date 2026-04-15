
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np
import os

from calcs import calcs

# --------------------------------------------------------------------------------------------------

def run_calc(n,input_file='nscf_template.py'):

    kwargs = {'num_electrons':n,
              'site_density_input_file':f'scf/pm_N_{n:3.2f}.hdf5',
              'electron_output_file':f'nscf/pm_N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

num_calcs = len(calcs)

for ii in range(num_calcs):
    
    n, U, order = calcs[ii]

    n *= 2.0

    print(f'\nnow on num {ii}/{num_calcs}')

    run_calc(n)

# --------------------------------------------------------------------------------------------------



