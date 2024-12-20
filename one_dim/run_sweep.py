
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

for n in [100]: #enumerate(num_sc):

    sc_dir = f'{n}x1'

    for h in [2/100.0]: #num_holes:

        doping_dir = os.path.join(sc_dir,f'{h:.4f}')
       
        # ------------------------------------------------------------------------------------------

        model_file = f'scf_n_{n}_h_{h:.4f}.py'
        ELPH = c_ELPH(os.path.join(doping_dir,model_file))
        ELPH.set_config()
        ELPH.run()

        model_file = f'restart_n_{n}_h_{h:.4f}.py'
        ELPH = c_ELPH(os.path.join(doping_dir,model_file))
        ELPH.set_config()
        ELPH.run()

        model_file = f'nscf_n_{n}_h_{h:.4f}.py'
        ELPH = c_ELPH(os.path.join(doping_dir,model_file))
        ELPH.set_config()
        ELPH.run()

        # ------------------------------------------------------------------------------------------