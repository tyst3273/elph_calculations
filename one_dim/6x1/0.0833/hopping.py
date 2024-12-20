# set hopping between the atoms. hopping param t is set for atoms of types type-1 and
# type-2 if they are within distance r-min to r-max of one-another. note that r-max sets the 
# cutoff for how far to search for NN bonds
# --------------------------------------------------------------------------------------------------
#                   type-1  n-1  l-1  m-1  type-2  n-2  l-2  m-2    t  r-min  r-max 

hopping_params = [  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,     1.0,   0.9,   1.1]

#hopping_params = [  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,    0.5,   0.9,   1.1]

#hopping_params = [[  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,    0.5,   0.9,   1.1],
#                  [  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,  -0.05,   1.3,   1.5],
#                  [  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,   0.1,   1.9,   2.1]]

#hopping_params = [[  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,    0.5,   0.9,   1.1],
#                  [  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,  -0.05,   1.3,   1.5]]

#hopping_params = [[  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,    0.5,   0.9,   1.1],
#                  [  'Cu',   1,   0,   0,   'Cu',   1,   0,   0,   0.05,   1.9,   2.1]]

