
# custom modules
from elph.drivers.m_ELPH import c_ELPH

# must be done after import c_ELPH
import numpy as np

# --------------------------------------------------------------------------------------------------

def run_calc(n,input_file='nscf_template.py'):

    kwargs = {'num_electrons':n,
              'electron_output_file':f'N_{n:3.2f}.hdf5'}
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------

calcs = np.arange(0.05,2.0,0.05)
num_calcs = len(calcs)

for ii in range(num_calcs):
    
    n = calcs[ii]
    run_calc(n)

# --------------------------------------------------------------------------------------------------



