
import numpy as np
import matplotlib.pyplot as plt
import os

# custom modules
from elph.drivers.m_ELPH import c_ELPH
from plot_fs import plot_fs

# template to get args from
scf_template = 'scf_template.py'
nscf_template = 'nscf_template.py'

num_electrons = np.linspace(0.1,1.0,10)

num_calcs = num_electrons.size
for ii, n in enumerate(num_electrons):

    scf_output_file = f'scf_prim_num_e_{n:2.1f}.hdf5'
    nscf_output_file = f'nscf_prim_num_e_{n:2.1f}.hdf5'

    # run scf calc
    kwargs = {'num_electrons':n,
              'electron_output_file':scf_output_file}
    ELPH = c_ELPH(scf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # run nscf calc
    kwargs = {'num_electrons':n,
              'site_density_input_file':scf_output_file,
              'electron_output_file':nscf_output_file}
    ELPH = c_ELPH(nscf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()

    plot_fs(nscf_output_file)

# --------------------------------------------------------------------------------------------------



