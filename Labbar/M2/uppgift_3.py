import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = 1 + x + 4/((x - 2)**2)
ay = x + 1

plt.plot(x, y)
plt.plot([2, 2], [-10, 10])
plt.plot(x, ay)

plt.axis([-10, 10, -10, 10])
plt.show()