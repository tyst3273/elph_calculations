
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

def make_Cu_file(U):
    with open('Cu_template.py','r') as f:
        lines = f.readlines()
    with open('Cu.py','w') as f:
        for line in lines:
            if not line.strip().startswith('hubbard_U'):
                f.write(line)
                continue
            else:
                line = f'hubbard_U = [{U:.4f}]\n'
                f.write(line)


# template to get args from
scf_template = 'scf_template.py'
nscf_template = 'nscf_template.py'
restart_template = 'restart_template.py'

# initial unitcell
pos = [[ 0.0, 0.0, 0.0]]
vecs = [[ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0],
        [ 0.0, 0.0,10.0]]
types = ['Cu']

#num_sc = np.array([4,6,8,10,16,20],dtype=float)
#num_holes = 2/num_sc

n = 8
h = 0.25

U_vals = np.arange(2.0,9.0,1.0)

for jj, U in enumerate(U_vals):

    U_dir = f'U_{U:.4f}'
    if not os.path.exists(U_dir):
        os.mkdir(U_dir)

    # ------------------------------------------------------------------------------------------

    make_Cu_file(U)
    os.rename('Cu.py',f'./{U_dir}/Cu.py')

    shutil.copy('hopping.py',f'./{U_dir}/hopping.py')

    # start from afm ground state
    stripes = c_stripes(pos,vecs,types,h,[n,n,1])
    stripes.neel_order()
    kwargs = stripes.get_model_kwargs()

    num_sites = len(kwargs['atom_types'])
    num_electrons = num_sites*(1-h)
        
    model_file = f'scf_n_{n}_U_{U:.4f}.py'
    scf_output_file = f'scf_n_{n}_U_{U:.4f}.hdf5'
    kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons})
    ELPH = c_ELPH(scf_template)
    ELPH.set_config(**kwargs)
    ELPH.write_config(model_file)
    os.rename(model_file,f'./{U_dir}/'+model_file)

    model_file = f'restart_n_{n}_U_{U:.4f}.py'
    restart_output_file = f'restart_n_{n}_U_{U:.4f}.hdf5'
    kwargs.update({'electron_output_file':restart_output_file,
                    'num_electrons':num_electrons,
                   'site_density_input_file':scf_output_file})
    ELPH = c_ELPH(restart_template)
    ELPH.set_config(**kwargs)
    ELPH.write_config(model_file)
    os.rename(model_file,f'./{U_dir}/'+model_file)

    model_file = f'nscf_n_{n}_U_{U:.4f}.py'
    nscf_output_file = f'nscf_n_{n}_U_{U:.4f}.hdf5'
    kwargs.update({'electron_output_file':nscf_output_file,
                    'num_electrons':num_electrons,
                    'site_density_input_file':restart_output_file})
    ELPH = c_ELPH(nscf_template)
    ELPH.set_config(**kwargs)
    ELPH.write_config(model_file)
    os.rename(model_file,f'./{U_dir}/'+model_file)

    # ------------------------------------------------------------------------------------------

