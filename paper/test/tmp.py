import numpy as np
import matplotlib.pyplot as plt

d1 = np.loadtxt('tmp_1.txt',dtype=complex)
d2 = np.loadtxt('tmp_2.txt',dtype=complex)

diff = d1[:,0]-d2[:,0]
real = diff.real
imag = diff.imag

plt.plot(real,c='r')
plt.plot(imag,c='b')

plt.show()