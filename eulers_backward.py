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

    y[0] = initial_val

    for i in range(len(x) - 1):
        x_o, y_o = x[i], y[i]
        x_f = x[i+1]
        y_f = y_o + h * f(x_o, y_o) # Use Euler's forward method as an estimate for the next y val

        y[i + 1] = optimize.fsolve(F, y_f, args=(f, x_f, y_o, h))
    
    mp.plot(x,y)
    mp.show()

    return x, y


def F(y_f, f, x_f, y_o, h):
    # The equation to solve for y_f
    return y_f - y_o - f(x_f, y_f) * h

def g(x, y):
    return -2 * y

def f(x, y):
    return x + 2 * y

# Sample call:
print(eulers_backward(f,0,9,0.1,1))

# Sample call:
#print(eulers_backward(g,0,2,0.2,1))

