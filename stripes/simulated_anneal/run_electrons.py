
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

num_sc = np.array([4,6,8,10,16,20],dtype=float)
num_holes = 2/num_sc

num_calcs = len(num_sc)
for ii, n in enumerate(num_sc):

    print(f'\nnow on num {ii}/{num_calcs}')

    # stripe model
    stripes = c_stripes(pos,vecs,types,0.0,[n,n,1])
    stripes.neel_order()
    stripes.write(f'{n}x{n}_model.txt')
    kwargs = stripes.get_model_kwargs()
    num_electrons = len(kwargs['atom_types']) # half filling

    # number of holes in primitive cell (filling fraction)
    h = num_holes[ii] 

    _nk = round(40/n) 
    if _nk % 2 != 0:
        _nk += 1
    kpts_mesh = [_nk,_nk,1]
   
#    print(kpts_mesh)
#    continue

    # scf
    scf_output_file = f'scf_n_{n}_h_{h:3f}.hdf5'
    kwargs.update({'electron_output_file':scf_output_file,
                   'num_electrons':num_electrons*(1-h),
                   'kpts_mesh':kpts_mesh})
    ELPH = c_ELPH(scf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()
    
    continue

    _nk = round(80/n)
    if _nk % 2 != 0:
        _nk += 1
    kpts_mesh = [_nk,_nk,1]
    print(kpts_mesh)

    # nscf
    nscf_output_file = f'nscf_sc_{num_sc}_n_{n}.hdf5'
    kwargs.update({'electron_output_file':nscf_output_file,
                   'site_density_input_file':scf_output_file,
                   'num_electrons':num_electrons*(1-h)})
    ELPH = c_ELPH(nscf_template)
    ELPH.set_config(**kwargs)
    ELPH.run()






