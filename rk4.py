import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Define the function for the differential equation
def f(x):
    return np.sin(np.abs(x - 1))

# Analytical solution
def analytical_solution(x):
    y = np.zeros_like(x)
    for i, xi in enumerate(x):
        if xi < 1:
            y[i], _ = quad(lambda t: np.sin(1 - t), 0, xi)
        else:
            y[i], _ = quad(lambda t: np.sin(t - 1), 0, xi)
    return y

# RK4 method
def rk4(f, x0, y0, x_end, h):
    x = np.arange(x0, x_end, h)
    y = np.zeros(x.shape)
    y[0] = y0
    for i in range(1, len(x)):
        k1 = h * f(x[i-1])
        k2 = h * f(x[i-1] + 0.5 * h)
        k3 = h * f(x[i-1] + 0.5 * h)
        k4 = h * f(x[i-1] + h)
        y[i] = y[i-1] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return x, y

# Parameters
x0, y0 = 0, 0  # initial conditions
x_end = 2 * np.pi
h = 0.01  # step size

# Analytical solution
x_analytical = np.arange(x0, x_end, h)
y_analytical = analytical_solution(x_analytical)

# Numerical solution using RK4
x_rk4, y_rk4 = rk4(f, x0, y0, x_end, h)

# Plotting both solutions
plt.figure(figsize=(10, 6))
plt.plot(x_analytical, y_analytical, label='Analytical Solution')
plt.plot(x_rk4, y_rk4, '--', label='RK4 Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of dy/dx = sin(|x-1|)')
plt.legend()
plt.grid(True)
plt.show()
