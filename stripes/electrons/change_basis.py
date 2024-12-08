import numpy as np


A_prim = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 10]],dtype=float)
A_stripes = np.array([[4, 0, 0],[0, 4, 0],[0, 0, 10]],dtype=float)

B_prim = np.linalg.inv(A_prim.T)
B_stripes = np.linalg.inv(A_stripes.T)

Q_prim = np.array([[4,0,0],
                  [6,0,0],
                  [4,4,0],
                  [6,6,0],
                  [4,6,0],
                  [6,4,0]],dtype=float)

M = np.linalg.inv(B_stripes)@B_prim

for ii in range(Q_prim.shape[0]):
    Q = Q_prim[ii,:]
    Q_stripes = M@Q
    print(Q_stripes)


