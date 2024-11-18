
import numpy as np
import sys

# path = '/Users/ty/research/repos/elph/elph_tools'
# sys.path.append(path)

# this is in ~/research/repos/elph/
from elph_tools.make_stripes import c_stripes


# define primitive unitcell
pos = [[ 0.0, 0.0, 0.0],
       [ 0.5, 0.0, 0.0],
       [ 0.0, 0.5, 0.0]]
vecs = [[ 1.0, 0.0, 0.0],
        [ 0.0, 1.0, 0.0],
        [ 0.0, 0.0,10.0]]
types = ['Cu','O','O']
num_holes = 0.0

# define supercell
nx = 4; ny = 2
mult = [nx,ny,1]

# class for the model
stripes = c_stripes(pos,vecs,types,num_holes,mult)

# paramagnetic order
#stripes.pm_order()

# set underlying AFM order
stripes.neel_order()

# ferromagnetic order
#stripes.fm_order()

# set spin-density wave order
n = 8
q = [1/nx,0,0]
stripes.sdw_order(q)

# set charge-density wave order
q = [2/nx,0,0]
stripes.cdw_order(q)

# show the model
stripes.plot_model()

# write the model
stripes.write('model.txt')
    


