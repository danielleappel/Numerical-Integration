import numpy as np
import matplotlib.pyplot as plt
from eulers_forward_second_order import eulers_forward_2nd_order
from eulers_backward_second_order import eulers_backward_2nd_order
import math

# The differential equation to examine
def f_prime_prime(x, y, y_prime):
    return -4*y_prime - 4*y + math.e**(2*x)

# The solution to f_prime_prime
def f(x):
    return 15/16 * math.e**(-2*x) + (15 * math.e**(-2*x) * x)/4 + 1/16 * math.e**(2*x)

# Set up calls to Euler's method:
x0, xf = 0, 9
h, y0, y_prime0 = 0.1, 1, 2

x, y_f = eulers_forward_2nd_order(f_prime_prime, x0, xf, h, y0, y_prime0)
x, y_b = eulers_backward_2nd_order(f_prime_prime, x0, xf, h, y0, y_prime0)

# Calculate exact solution
y_exact_vector = np.array([f(i) for i in x])

# Plot solutions
plt.plot(x, y_f, marker='o', label='Euler\'s Forward Method')
plt.plot(x, y_b, label='Euler\'s Backward Method')
plt.plot(x, y_exact_vector, label='Exact solution')

plt.suptitle('Comparing Solutions')
plt.title(r'$y\prime\prime=-4y\prime-4y+e^{2x}$, $y(0)=1$, $y\prime(0)=2$ $\Rightarrow y=\frac{15}{16}e^{-2x}+\frac{15e^{-2x}x}{4}+\frac{1}{16}e^{2x}$')
plt.legend()
plt.show()

# Calculate errors and plot to compare the two methods
error_f = abs(y_exact_vector - y_f)
error_b = abs(y_exact_vector - y_b)

plt.plot(x, error_f, marker='o', label='Euler\'s Forward Method')
plt.plot(x, error_b, label='Euler\'s Backward Method')

plt.suptitle('Errors')
plt.title(r'$y\prime\prime=-4y\prime-4y+e^{2x}$')
plt.legend()
plt.show()

# Calculate the error ratio and plot to compare
error_ratio_f = error_f[:-1]/error_f[1:]
error_ratio_b = error_b[:-1]/error_b[1:]

plt.plot(x[:-1], error_ratio_f, label='Euler\'s Forward Method')
plt.plot(x[:-1], error_ratio_b, label='Euler\'s Backward Method')

plt.suptitle('Error ratios')
plt.title(r'Error ratio for $y\prime\prime=-4y\prime-4y+e^{2x}$')
plt.legend()
plt.show()
