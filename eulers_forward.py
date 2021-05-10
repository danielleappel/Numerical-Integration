# Euler's Method
import numpy as np
import matplotlib.pyplot as mp

def eulers_forward(f, x_start, x_stop, h, initial_val):
    """ Returns the x and y vectors from euler's forward method
        given a function f, start and stop values for x, step size, and initial value of y
    """
    x = np.arange(x_start, x_stop + h, h)
    y = [0] * len(x)

    y[0] = initial_val

    for i in range(len(y) - 1):
        y[i+1] = y[i] + h * f(x[i], y[i])

    mp.plot(x,y)
    mp.show()

    return x, y

def f(x, y):
    return x + 2 * y



# Sample call:
print(eulers_forward(f,0,9,0.45,1))
