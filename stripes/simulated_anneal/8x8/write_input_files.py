
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

#num_sc = np.array([4,6,8,10,16,20],dtype=float)
#num_holes = 2/num_sc

num_sc = np.array([8])
num_holes = [0.0625, 0.125, 0.25, 1/3., 0.5]

step = 0
num_calcs = len(num_sc)*len(num_holes)
for ii, n in enumerate(num_sc):
    for jj, h in enumerate(num_holes):

        print(f'\nnow on num {step}/{num_calcs}')

        # ------------------------------------------------------------------------------------------

        # start from afm ground state
        stripes = c_stripes(pos,vecs,types,h,[n,n,1])
        stripes.neel_order()
        kwargs = stripes.get_model_kwargs()

        num_sites = len(kwargs['atom_types'])
        num_electrons = num_sites*(1-h)

        
        model_file = f'scf_n_{n}_h_{h:.4f}.py'
        scf_output_file = f'scf_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons})
        ELPH = c_ELPH(scf_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        #ELPH.run()

        model_file = f'nscf_n_{n}_h_{h:.4f}.py'
        nscf_output_file = f'nscf_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons,
                       'site_density_input_file':scf_output_file})
        ELPH = c_ELPH(nscf_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        #ELPH.run()

        # ------------------------------------------------------------------------------------------

