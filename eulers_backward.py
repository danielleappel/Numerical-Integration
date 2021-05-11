# Euler's Method
import numpy as np
import matplotlib.pyplot as mp
from scipy import optimize

def eulers_backward(f, x_start, x_stop, h, initial_val):
    """ Returns the x and y vectors from euler's backward method
        given a function f, start and stop values for x, step size, and initial value of y
    """
    x = np.arange(x_start, x_stop + h, h)
    y = np.zeros(len(x))

    for i in range(len(x) - 1):
        yp = y[i] + h * f(x[i],y[i])
        y[i + 1] = optimize.fsolve(F, yp, args=(f, x[i+1], y[i], h))
        print(y[i+1])


def F(y1, f, x1, y0, h):
    return y1 - f(x1, y1) * h - y0

def g(x, y):
    return -2 * y
print(eulers_backward(g,0,2,0.2,1))
x=1
print(optimize.fsolve(g, 0, args=(x)))