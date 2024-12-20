
# custom modules
from elph.drivers.m_ELPH import c_ELPH
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

n = 8
U_vals = np.arange(2.0,9.0,1.0)
#U_vals = np.linspace(4.0,8.0,9)

for jj, U in enumerate(U_vals):

    if U < 6:
        continue

    U_dir = f'U_{U:.4f}'
    os.chdir(U_dir)

    model_file = f'scf_n_{n}_U_{U:.4f}.py'
    ELPH = c_ELPH(model_file)
    ELPH.set_config()
    ELPH.run()

    model_file = f'restart_n_{n}_U_{U:.4f}.py'
    ELPH = c_ELPH(model_file)
    ELPH.set_config()
    ELPH.run()

#    model_file = f'nscf_n_{n}_U_{U:.4f}.py'
#    ELPH = c_ELPH(model_file)
#    ELPH.set_config()
#    ELPH.run()

    os.chdir('..')

    # ------------------------------------------------------------------------------------------

