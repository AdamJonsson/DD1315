import numpy as np
import matplotlib.pyplot as plt
from tools import clearPrint

def calcReimanSum(funcValue, xValue):
    theSum = 0
    for index in range(len(xValue) - 1):
        theSum += funcValue.item(index) * (xValue.item(index + 1) - xValue.item(index))
    return theSum

dx = 0.1
x1 = np.arange(0, 2, dx)
x2 = np.arange(1, 4, dx)

y1 = x1 / (x1**2 + 4)**(1/3); correctY1 = 3 - 3/(2**(2/3))
y2 = np.sqrt(x2) * np.log(x2); correctY2 = 16*np.log(4)/3 - 28/9

reimanSumY1 = calcReimanSum(y1, x1)
reimanSumY2 = calcReimanSum(y2, x2)

clearPrint("ReimanSumY1", (correctY1 - reimanSumY1))
clearPrint("ReimanSumY2", (correctY2 - reimanSumY2))