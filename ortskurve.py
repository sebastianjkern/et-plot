import matplotlib.pyplot as plt
import numpy as np

r1 = .1
r2 = .1
L = .1
w = 1
C = .1

# data = 1 / (r1 + 1/(1j*w*np.arange(0.1, 1000000, 1.5) + 1/(1j*w*L + r2)))
data = 1j * w * C + 1/(1j*w*L + 1/np.arange(0.1, 10000, .5))

x = data.real
y = data.imag

plt.plot(x, y)
plt.axis('square')

plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()

