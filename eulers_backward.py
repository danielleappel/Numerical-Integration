# Euler's Method
import numpy as np
import matplotlib.pyplot as mp
from scipy.optimize import fsolve

def eulers_forward(f, x_start, x_stop, initial_val):
    h = 0.45      # step size
    x = np.arange(x_start, x_stop + h, h)
    y = [0] * len(x)

    y[0] = initial_val

    for i in range(len(y) - 1):
        y[i+1] = y[i] + h * f_solve()


    mp.plot(x,y)
    mp.show()

    return y

def f(x, y):
    return x + 2 * y




# Sample call:
print(eulers(f,0,9,1))
