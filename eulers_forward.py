# Euler's Method
import numpy as np

def eulers_forward(f, x_start, x_stop, h, initial_val):
    """ Returns the x and y vectors from euler's forward method
        given a function f, start and stop values for x, step size, and initial value of y
    """
    x = np.arange(x_start, x_stop + h, h)
    y = np.zeros(len(x))

    y[0] = initial_val

    for i in range(len(y) - 1):
        y[i+1] = y[i] + h * f(x[i], y[i])
    
    return x, y