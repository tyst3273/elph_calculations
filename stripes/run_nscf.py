
import numpy as np
import matplotlib.pyplot as plt
import os

# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

# template to get args from
input_file = 'scf_template.py'

# initial unitcell
pos = [[ 0.0, 0.0, 0.0],
       [ 0.5, 0.0, 0.0],
       [ 0.0, 0.5, 0.0]]
vecs = [[ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0],
        [ 0.0, 0.0,10.0]]
types = ['Cu','O','O']
num_holes = 0.1 # number of holes in primitive cell

# diagonal stripes
num_sc = 4
mult = [num_sc,num_sc,1]
q_sdw = np.arange(1,num_sc/2+1) # from 1 to num_sc/2

stripes = c_stripes(pos,vecs,types,num_holes,mult)

# loop over sdw wavevecs
num_calcs = q_sdw.size
for ii, q in enumerate(q_sdw):
    
    stripes.neel_order()
    stripes.sdw_order([q/num_sc,q/num_sc,0])
    stripes.cdw_order([2*q/num_sc,2*q/num_sc,0])

    print(f'\nnow on num {ii}/{num_calcs}')
    print(f'q=',q)
    
    # get kwargs from stripes class
    kwargs = stripes.get_model_kwargs()
    kwargs.update({'electron_output_file':'scf_sc_{num_sc}_q_{q}_diagonal.hdf5'})
    ELPH = c_ELPH(input_file)
    ELPH.set_config(**kwargs)
    ELPH.run()

# --------------------------------------------------------------------------------------------------



