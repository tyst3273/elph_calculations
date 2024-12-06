import numpy as np


A_HTT = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 10]],dtype=float)
A_LTT = np.array([[1, -1, 0],[1, 1, 0],[0, 0, 10]],dtype=float)

B_HTT = np.linalg.inv(A_HTT.T)
B_LTT = np.linalg.inv(A_LTT.T)

Q_HTT = np.array([[3,3,0],
                  [5,5,0],
                  [2,4,0],
                  [4,2,0],
                  [3,0,0],
                  [5,0,0]],dtype=float)

M = np.linalg.inv(B_LTT)@B_HTT

for ii in range(Q_HTT.shape[0]):
    Q = Q_HTT[ii,:]
    Q_LTT = M@Q
    print(Q_LTT)


