import numpy as np
import math
import matplotlib.pyplot as plt
from tools import clearPrint

x = np.arange(-10, 10, 0.1)
y = np.sin(x)
plt.plot(x, y)

taylorY = np.zeros(200)
print(taylorY)
for k in range(7):
    newValue = ((-1)**k * x**(1 + 2*k))/(math.factorial(1 + 2*k))
    taylorY = np.add(taylorY, newValue)

plt.plot(x, taylorY)
plt.axis([-10, 10, -10, 10])
plt.show()