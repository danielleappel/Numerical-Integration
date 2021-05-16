# Euler's Method
import numpy as np
import matplotlib.pyplot as mp
import math

def eulers_forward_second_order(f, x_start, x_stop, h, initial_val_y, initial_val_y_prime):
    """ Returns the x and y vectors from euler's forward method
        given a function f, start and stop values for x, step size, and initial value of y
    """
    x = np.arange(x_start, x_stop + h, h)
    y = np.zeros(len(x))
    y_prime = np.zeros(len(x))

    y[0] = initial_val_y
    y_prime[0] = initial_val_y_prime

    for i in range(len(y) - 1):
        y[i + 1] = y[i] + h*y_prime[i]
        y_prime[i + 1] = y_prime[i] + h * f(x[i], y[i], y_prime[i])

    mp.plot(x,y)
    mp.show()

    return x, y

def f(x, y, y_prime):
    return -4*y_prime - 4*y + math.e**(2*x)

# Sample call:
print(eulers_forward_second_order(f,0,10,0.1,1,0))
