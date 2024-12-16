
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt
import os

# template to get args from
scf_template = 'scf_template.py'
nscf_template = 'nscf_template.py'

# initial unitcell
pos = [[ 0.0, 0.0, 0.0]]
vecs = [[ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0],
        [ 0.0, 0.0,10.0]]
types = ['Cu']

num_holes = [32] # number of holes in supercell

# diagonal stripes
num_sc = 16
mult = [num_sc,num_sc,1]

stripes = c_stripes(pos,vecs,types,0.0,mult)
stripes.neel_order()
kwargs = stripes.get_model_kwargs()
num_electrons = len(kwargs['atom_types']) # half filling

# loop over sdw wavevecs
num_calcs = len(num_holes)
for ii, n in enumerate(num_holes):
    
    print(f'\nnow on num {ii}/{num_calcs}')

    # scf
    scf_output_file = f'scf_sc_{num_sc}_n_{n}.hdf5'
    kwargs.update({'electron_output_file':scf_output_file,
                   'num_electrons':num_electrons-n})
    ELPH = c_ELPH(scf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()

    # nscf
    nscf_output_file = f'nscf_sc_{num_sc}_n_{n}.hdf5'
    kwargs.update({'electron_output_file':nscf_output_file,
                   'site_density_input_file':scf_output_file,
                   'num_electrons':num_electrons-n})
    ELPH = c_ELPH(nscf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()

