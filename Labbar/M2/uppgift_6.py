import numpy as np
import matplotlib.pyplot as plt
from tools import clearPrint

def diffFunction(t, A, B):
    return np.exp(-1 * t) * (A * np.cos(t) + B* np.sin(t)) + np.cos(t) + 2*np.sin(t)  

t = np.arange(0, 10, 0.1)
A = np.arange(-4, 4, 1); B = np.arange(-4, 4, 1)

for a in A:
    for b in B:
        y = diffFunction(t, a, b)
        plt.plot(t, y)

testY = np.cos(t) + 2*np.sin(t)
plt.plot(t, testY, dashes=[2, 2], color="blue")

plt.show()