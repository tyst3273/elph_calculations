import numpy as np

n = np.arange(1,21)
h = 2/n
print(h)
print(n)

for ii in range(h.size):
    print(f'num_sc: {n[ii]:6}, num_holes: {h[ii]:6.3f}')

