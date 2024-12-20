
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import shutil
import numpy as np
import matplotlib.pyplot as plt
import os

# template to get args from
scf_template = 'scf_template.py'
nscf_template = 'nscf_template.py'
restart_template = 'restart_template.py'

# initial unitcell
pos = [[ 0.0, 0.0, 0.0]]
vecs = [[ 1.0,  0.0, 0.0],
        [ 0.0, 10.0, 0.0],
        [ 0.0,  0.0,10.0]]
types = ['Cu']

num_sc = np.union1d(np.union1d(np.arange(4,26,2),np.arange(3,24,3)),np.arange(50,300,50))
print('num_sc:',num_sc)

num_holes = 2/num_sc
print('num_holes:',num_holes)

step = 0
num_calcs = len(num_sc)*len(num_holes)

for ii, n in enumerate(num_sc):

    sc_dir = f'{n}x1'
    if not os.path.exists(sc_dir):
        os.mkdir(sc_dir)

    kpts_mesh = int(1000/np.sqrt(n))
    if kpts_mesh % 2 != 0:
        kpts_mesh += 1
    kpts_mesh = [kpts_mesh,1,1]

    for jj, h in enumerate(num_holes):

        doping_dir = os.path.join(sc_dir,f'{h:.4f}')
        if not os.path.exists(doping_dir):
            os.mkdir(doping_dir)

        print(f'\nnow on num {step}/{num_calcs}')

        shutil.copy('hopping.py',doping_dir)
        shutil.copy('Cu.py',doping_dir)

        # ------------------------------------------------------------------------------------------

        # start from afm ground state
        stripes = c_stripes(pos,vecs,types,h,[n,1,1])
        stripes.neel_order()
        kwargs = stripes.get_model_kwargs()

        num_sites = len(kwargs['atom_types'])
        print(h)
        num_electrons = num_sites*(1-h)
        print(num_sites)
        print(f'num_electrons:',num_electrons)

        model_file = f'scf_n_{n}_h_{h:.4f}.py'
        scf_output_file = f'scf_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons,
                       'kpts_mesh':kpts_mesh})
        ELPH = c_ELPH(scf_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        os.rename(model_file,os.path.join(doping_dir,model_file))

        model_file = f'restart_n_{n}_h_{h:.4f}.py'
        restart_output_file = f'restart_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':restart_output_file,
                       'num_electrons':num_electrons,
                       'site_density_input_file':scf_output_file,
                       'kpts_mesh':kpts_mesh})
        ELPH = c_ELPH(restart_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        os.rename(model_file,os.path.join(doping_dir,model_file))

        model_file = f'nscf_n_{n}_h_{h:.4f}.py'
        nscf_output_file = f'nscf_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':nscf_output_file,
                       'num_electrons':num_electrons,
                       'site_density_input_file':restart_output_file,
                       'kpts_mesh':kpts_mesh})
        ELPH = c_ELPH(nscf_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        os.rename(model_file,os.path.join(doping_dir,model_file))

        # ------------------------------------------------------------------------------------------

