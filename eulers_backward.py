# Euler's Method
import numpy as np
import matplotlib.pyplot as mp

def eulers_forward(f, x_start, x_stop, h, initial_val):
    """ Returns the x and y vectors from euler's backward method
        given a function f, start and stop values for x, step size, and initial value of y
    """
    x = np.arange(x_start, x_stop + h, h)
    y = [0] * len(x)