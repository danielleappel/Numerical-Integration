import numpy as np
import matplotlib.pyplot as plt
from eulers_forward import eulers_forward
from eulers_backward import eulers_backward
import math

# The differential equation to examine
def f_prime(x, y):
    return x + 2 * y

# The solution to f_prime
def f(x):
    return -(2*x + 1)/4 + (5/4)*math.e**(2*x)

# Set up calls to Euler's method:
x0, xf = 0, 9
h, y0 = 0.1, 1

x, y_f = eulers_forward(f_prime, x0, xf, h, y0)
x, y_b = eulers_backward(f_prime, x0, xf, h, y0)

# Calculate exact solution
y_exact_vector = np.array([f(i) for i in x])

# Plot solutions
plt.plot(x, y_f, label='Euler\'s Forward Method')
plt.plot(x, y_b,label='Euler\'s Backward Method')
plt.plot(x, y_exact_vector, label='Exact solution')

plt.suptitle('Comparing Solutions')
plt.title(r'$y\prime=x+2y$, $y(0)=1$ $\Rightarrow y=-\frac{2x+1}{4}+\frac{5}{4}e^{2x}$')
plt.legend()
plt.show()

# Calculate errors and plot to compare the two methods
error_f = abs(y_exact_vector - y_f)
error_b = abs(y_exact_vector - y_b)

plt.plot(x, error_f, label='Euler\'s Forward Method')
plt.plot(x, error_b, label='Euler\'s Backward Method')

plt.suptitle('Errors')
plt.title(r'Error for $y\prime=x+2y$')
plt.legend()
plt.show()

# Calculate the error ratio and plot to compare
error_ratio_f = error_f[:-1]/error_f[1:]
error_ratio_b = error_b[:-1]/error_b[1:]

plt.plot(x[:-1], error_ratio_f, label='Euler\'s Forward Method')
plt.plot(x[:-1], error_ratio_b, label='Euler\'s Backward Method')

plt.suptitle('Error ratios')
plt.title(r'Error ratio for $y\prime=x+2y$')
plt.legend()
plt.show()