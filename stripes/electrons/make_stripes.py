
from elph_tools.m_make_stripes import c_stripes

import numpy as np
import matplotlib.pyplot as plt

# define primitive unitcell
pos = [[ 0.0, 0.0, 0.0],
       [ 0.5, 0.0, 0.0],
       [ 0.0, 0.5, 0.0]]
vecs = [[ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0],
        [ 0.0, 0.0,10.0]]
types = ['Cu','O','O']
num_holes = 0.0 # number of holes in primitive cell

# define supercell
nx = 12; ny = 12
mult = [nx,ny,1] # multiplicity

# class for the model
stripes = c_stripes(pos,vecs,types,num_holes,mult)

# paramagnetic order
#stripes.pm_order()

# set underlying AFM order
stripes.neel_order()

# ferromagnetic order
#stripes.fm_order()

# set spin-density wave order
n = 10
q = [2*n/nx,0,0]
stripes.sdw_order(q)

# set charge-density wave order
q = [n/nx,0,0]
stripes.cdw_order(q)

# show the model
stripes.plot_model_2D()

# write the model
stripes.write('model.txt')
    


