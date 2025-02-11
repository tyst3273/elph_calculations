
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt
import os

# template to get args from
scf_template = 'scf_template.py'
nscf_template = 'nscf_template.py'
restart_template = 'restart_template.py'

# initial unitcell
pos = [ [ 0.0, 0.0, 0.0],
        [ 0.5, 0.0, 0.0],
        [ 0.0, 0.5, 0.0] ]
vecs = [ [ 1.0, 0.0, 0.0],
         [ 0.0, 1.0, 0.0],
         [ 0.0, 0.0,10.0] ]
types = ['Cu','O','O']

electron_scf_density_tol = 1e-4
electron_scf_energy_tol = 1e-5
num_kpts = 1000

num_sc = np.array([2,4,6,8,10]) #,16,20,40])
num_holes = 2/num_sc
num_holes[0] = 0.95

step = 0
num_calcs = len(num_sc)*len(num_holes)
for ii, n in enumerate(num_sc):
    for jj, h in enumerate(num_holes):

        print(f'\nnow on num {step}/{num_calcs}')

        # start from afm ground state
        stripes = c_stripes(pos,vecs,types,h,[n,n,1])
        stripes.neel_order()
        kwargs = stripes.get_model_kwargs()

        num_sites = np.flatnonzero(kwargs['atom_types'] == 'Cu').size
        num_electrons = num_sites*(1-h)

        # ------------------------------------------------------------------------------------------

        _energy_tol = electron_scf_energy_tol*n**2
        _density_tol = electron_scf_density_tol*n**2
        _num_kpts = num_kpts/n**2
        if _num_kpts % 2 != 0:
            _num_kpts += 1
        _kpts_mesh = [_num_kpts,_num_kpts,1]
        
        model_file = f'scf_n_{n}_h_{h:.4f}.py'
        scf_output_file = f'scf_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':scf_output_file,
                       'num_electrons':num_electrons,
                       'electron_scf_energy_tol':_energy_tol,
                       'electron_scf_density_tol':_density_tol,
                       'kpts_mesh':_kpts_mesh})
        ELPH = c_ELPH(scf_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        #ELPH.run()

        # ------------------------------------------------------------------------------------------

        _energy_tol = electron_scf_energy_tol*n**2/10
        _density_tol = electron_scf_density_tol*n**2/10
        _num_kpts = 2*num_kpts/n**2
        if _num_kpts % 2 != 0:
            _num_kpts += 1
        _kpts_mesh = [_num_kpts,_num_kpts,1]
        
        model_file = f'restart_n_{n}_h_{h:.4f}.py'
        restart_output_file = f'restart_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':restart_output_file,
                       'num_electrons':num_electrons,
                       'electron_scf_energy_tol':_energy_tol,
                       'electron_scf_density_tol':_density_tol,
                       'kpts_mesh':_kpts_mesh,
                       'site_density_input_file':scf_output_file})
        ELPH = c_ELPH(restart_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        #ELPH.run()

        # ------------------------------------------------------------------------------------------

        _num_kpts = 4*num_kpts/n**2
        if _num_kpts % 2 != 0:
            _num_kpts += 1
        _kpts_mesh = ls *[_num_kpts,_num_kpts,1]
        
        model_file = f'nscf_n_{n}_h_{h:.4f}.py'
        nscf_output_file = f'nscf_n_{n}_h_{h:.4f}.hdf5'
        kwargs.update({'electron_output_file':nscf_output_file,
                       'num_electrons':num_electrons,
                       'kpts_mesh':_kpts_mesh,
                       'site_density_input_file':restart_output_file})
        ELPH = c_ELPH(nscf_template)
        ELPH.set_config(**kwargs)
        ELPH.write_config(model_file)
        #ELPH.run()

        # ------------------------------------------------------------------------------------------