import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.05)
y = 1 + np.sin(x) + 0.5*np.cos(4*x)
dy = np.cos(x) - 2*np.sin(4*x)

calcDy = np.empty([])
for index in (range(len(x) - 1)):
    calcDy = np.append(calcDy, (y.item(index) - y.item(index + 1)) / (x.item(index) - x.item(index + 1)))

plt.plot(x, dy)
plt.plot(x, calcDy)
plt.show()
