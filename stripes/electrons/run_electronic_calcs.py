
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt
import os

# template to get args from
scf_template = 'scf_template.py'
nscf_template = 'nscf_template.py'
renorm_template = 'renorm_template.py'

# initial unitcell
pos = [[ 0.0, 0.0, 0.0],
       [ 0.5, 0.0, 0.0],
       [ 0.0, 0.5, 0.0]]
vecs = [[ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0],
        [ 0.0, 0.0,10.0]]
types = ['Cu','O','O']
num_holes = 0.15 # number of holes in primitive cell

# diagonal stripes
num_sc = 10
mult = [num_sc,num_sc,1]
#q_sdw = np.arange(1,num_sc/2+1) # from 1 to num_sc/2
q_sdw = np.array([1],dtype=float)

stripes = c_stripes(pos,vecs,types,num_holes,mult)

# loop over sdw wavevecs
num_calcs = q_sdw.size
for ii, q in enumerate(q_sdw):
    
    stripes.neel_order()
    stripes.sdw_order([q/num_sc,0,0])
    stripes.cdw_order([2*q/num_sc,0,0])

    print(f'\nnow on num {ii}/{num_calcs}')
    print(f'q=',q)
    
    scf_output_file = f'scf_sc_{num_sc}_q_{q}.hdf5'
    nscf_output_file = f'nscf_sc_{num_sc}_q_{q}.hdf5'
    renorm_output_file = f'renorm_sc_{num_sc}_q_{q}.hdf5'

    # get kwargs from stripes class
    kwargs = stripes.get_model_kwargs()
    
    """
    # run scf calc
    kwargs.update({'electron_output_file':scf_output_file})
    ELPH = c_ELPH(scf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()
    """

    # run nscf calc
    kwargs.update({'site_density_input_file':scf_output_file,
                   'electron_output_file':nscf_output_file})
    ELPH = c_ELPH(nscf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()


    """
    # run renorm calc
    kwargs.update({'site_density_input_file':nscf_output_file,
                   'electron_output_file':'tmp.hdf5',
                   'elph_output_file':renorm_output_file})
    ELPH = c_ELPH(renorm_template)
    ELPH.set_config(**kwargs)
    ELPH.run()
    """

# --------------------------------------------------------------------------------------------------

