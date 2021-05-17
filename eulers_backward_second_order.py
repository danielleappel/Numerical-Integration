# Euler's Method
import numpy as np
import matplotlib.pyplot as mp
from scipy import optimize
import math

def eulers_backward_2nd_order(f, x_start, x_stop, h, initial_val_y, initial_val_y_prime):
    """ Returns the x and y vectors from euler's backward method of a second order ODE
        given a function f, start and stop values for x, step size, and initial value of y and y_prime
    """
    x = np.arange(x_start, x_stop + h, h)
    y = np.zeros(len(x))
    y_prime = np.zeros(len(x))

    y[0] = initial_val_y
    y_prime[0] = initial_val_y_prime

    for i in range(len(x) - 1):
        x_n, y_n, y_prime_n = x[i], y[i], y_prime[i]
        x_n_1 = x[i+1]

        # Calculate the backwards y_b'
        y_b_prime = (y_n - y[i-1])/h

        # Use Euler's forward method as an estimate for y_f
        y_f = y_n + h * f(x_n, y_n, y_prime_n) 

        # Solve for the real value of y_f
        y[i + 1] = optimize.fsolve(F, y_f, args=(y[i-1], y_n, f, x_n, h))
    
    mp.plot(x,y)
    mp.show()

    return x, y


def F(y_2, y_0, y_1, f, x_2, h):
    """ The equation to solve for y_f in Euler's backward method """
    y_f = (y_2 - y_1)/h
    return y_2 + y_0 - 2*y_1 - f(x_2, y_2, y_f) * h**2


def f(x, y, y_prime):
    return -4*y_prime - 4*y + math.e**(2*x)

# Sample call:
print(eulers_backward_2nd_order(f,0,10,0.1,1,0))
