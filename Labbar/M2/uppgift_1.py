import numpy as np
from tools import clearPrint

a = np.arange(1, 6, 1)
clearPrint("a", a)

b = np.arange(0, 2*np.pi, 0.1)
clearPrint("b", b)

c = np.matrix("1 2 3; 4 5 6")
clearPrint("c", c)

d = np.append(a, [6,7])
clearPrint("d", d)

e = np.matrix([a, np.arange(-5, 0)])
clearPrint("e", e)

f = np.sin(b)
clearPrint("f", f)
