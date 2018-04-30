import numpy as np
from tools import *

def function_a(x):
    return x*x
clearPrint("Funktion_a", function_a(12))

def function_b1(x):
    return x*x
randVector = np.arange(0, 10)
clearPrint("Function_b1", function_b1(randVector))

def function_b2(x):
    return np.dot(x, x)
randVector = np.arange(0, 100, 5)
clearPrint("Funktion_b2", function_b2(randVector))

def function_c1(x):
    return np.multiply(x, x)
randMatrix = np.matrix("1 5 3 8; 9 3 2 1; 2 3 4 2")
clearPrint("Funktion_c1", function_c1(randMatrix))

def function_c2(x):
    return np.matmul(x, x)
randMatrix = np.matrix("1 1 1; 1 1 1; 1 1 1")
clearPrint("Funktion_c2", function_c2(randMatrix))