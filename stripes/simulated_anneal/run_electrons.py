
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
num_holes = 2/num_sc

step = 0
num_calcs = len(num_sc)*len(num_holes)
for ii, n in enumerate(num_sc):
    for jj, h in enumerate(num_holes):

        print(f'\nnow on num {step}/{num_calcs}')

        # ------------------------------------------------------------------------------------------

        # start from afm ground state
        stripes = c_stripes(pos,vecs,types,h,[n,n,1])
        stripes.neel_order()
        #stripes.write(f'{n}x{n}_model.txt')
        kwargs = stripes.get_model_kwargs()

        num_sites = len(kwargs['atom_types'])
        num_electrons = num_sites*(1-h)
        tol = num_sites*5e-4
        #start_temp = 1e-3+(num_sites-16)/48
        #end_temp = start_temp/20

        nk = round(40/n) 
        if nk % 2 != 0:
            nk += 1
        kpts_mesh = [nk,nk,1]

        print('num_electrons:',num_electrons)
        print('tol:',tol)
        print('kpts_mesh:',kpts_mesh)
#        print('start_temp:',start_temp)
#        print('end_temp:',end_temp)

        # scf
        scf_output_file = f'scf_n_{n}_h_{h:.3f}_afm.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons*(1-h),
                       'kpts_mesh':kpts_mesh,
                       'electron_scf_energy_tol':tol,
                       'electron_scf_density_tol':tol})
                       #'anneal_start_temperature':start_temp,
                       #'anneal_end_temperature':end_temp})
        ELPH = c_ELPH(scf_template)
        ELPH.set_config(**kwargs)
        ELPH.run()

        exit()

        # ------------------------------------------------------------------------------------------

        # start from fm ground state
        stripes.fm_order()
        kwargs = stripes.get_model_kwargs()

        # scf
        scf_output_file = f'scf_n_{n}_h_{h:.3f}_fm.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons*(1-h),
                       'kpts_mesh':kpts_mesh,
                       'electron_scf_energy_tol':tol,
                       'electron_scf_density_tol':tol})
                       #'anneal_start_temperature':start_temp,
                       #'anneal_end_temperature':end_temp})
        ELPH = c_ELPH(scf_template)
        ELPH.set_config(**kwargs)
        ELPH.run()

        # ------------------------------------------------------------------------------------------

        # start from pm ground state
        stripes.pm_order()
        kwargs = stripes.get_model_kwargs()

        # scf
        scf_output_file = f'scf_n_{n}_h_{h:.3f}_pm.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons*(1-h),
                       'kpts_mesh':kpts_mesh,
                       'electron_scf_energy_tol':tol,
                       'electron_scf_density_tol':tol})
                       #'anneal_start_temperature':start_temp,
                       #'anneal_end_temperature':end_temp})
        ELPH = c_ELPH(scf_template)
        ELPH.set_config(**kwargs)
        ELPH.run()

        # ------------------------------------------------------------------------------------------

        step += 1




