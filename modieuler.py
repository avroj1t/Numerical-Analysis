import numpy as np
import matplotlib.pyplot as plt

# Function to implement Modified Euler Method
def modified_euler(y0, x0, xEnd, h, f):
    y = y0
    x = x0
    xs = [x]
    ys = [y]

    while x < xEnd:
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        
        y = y + (h / 2) * (k1 + k2)
        x = x + h

        xs.append(x)
        ys.append(y)
    
    return np.array(xs), np.array(ys)

# Exact solution for comparison
def exact_solution(x, C):
    return (-1/2) * np.cos(2 * x) + C  # C is the constant of integration, in this case 0

# Parameters
y0 = 0.0    # Initial condition y(0)
x0 = 0.0    # Start value of x
xEnd = 1.0  # End value of x
h = 0.01     # Step size

# Differential equation function
def f(x, y):
    return np.sin(2 * x)

# Compute Modified Euler Method
xs, ys_mod_euler = modified_euler(y0, x0, xEnd, h, f)

# Compute exact solution for comparison
C = y0  # Constant of integration determined by initial condition
ys_exact = exact_solution(xs, C)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(xs, ys_exact, label='Exact Solution', color='blue', linestyle='--', marker='o')
plt.plot(xs, ys_mod_euler, label='Modified Euler Method', color='red', marker='s')
plt.title('Exact Solution vs Modified Euler Method')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
