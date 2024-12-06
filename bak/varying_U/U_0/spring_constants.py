# set spring constants between the atoms. spring constant K is set for atoms of types type-1 and
# type-2 if they are within distance r-min to r-max of one-another. note that r-max sets the 
# cutoff for how far to search for NN bonds
# --------------------------------------------------------------------------------------------------
#                     type-1   type-2      K          l,   r-min  r-max 
#spring_constants = [[   'Cu',     'O',  0.20,       0.5,   0.4,   0.6],
#                    [    'O',     'O',  0.02,  0.707106,   0.6,   0.8]]
spring_constants = [[   'Cu',     'O',  0.0150,       0.5,   0.4,   0.6],
                    [    'O',     'O',  0.0020,  0.707106,   0.6,   0.8]]


