import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def dydx(x, y):
    return np.log(x * y)

def runge_kutta_2(x0, y0, x, h):
    n = int((x - x0) / h)
    xs = [x0]
    ys = [y0]
    y = y0
    x_curr = x0

    for _ in range(n):
        k1 = h * dydx(x_curr, y)
        k2 = h * dydx(x_curr + h / 2, y + k1 / 2)
        y += k2
        x_curr += h

        xs.append(x_curr)
        ys.append(y)

        if np.isinf(y) or np.isnan(y):
            print(f"Numerical instability detected at x = {x_curr}")
            break

    return xs, ys

# Initial conditions
x0 = 1.0
y0 = 1.0
x_end = 2.0
h = 0.01

# RK2 solution
rk2_xs, rk2_ys = runge_kutta_2(x0, y0, x_end, h)

# Exact solution using solve_ivp
sol = solve_ivp(dydx, [x0, x_end], [y0], method='RK45', t_eval=np.linspace(x0, x_end, 1000))

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(rk2_xs, rk2_ys, 'bo-', label='RK2 Solution')
plt.plot(sol.t, sol.y[0], 'r-', label='Exact Solution (solve_ivp)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of RK2 Solution and Exact Solution')
plt.legend()
plt.grid(True)
plt.show()
