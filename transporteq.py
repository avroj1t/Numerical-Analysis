import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

c = 1
xmin = 0
xmax = 1
n = 50

X, dx = np.linspace(xmin, xmax, n, retstep=True)
dt = 0.1 * dx / c

def initial_u(x):
    return np.exp(-0.5 * np.power(((x - 0.5) / 0.08), 2))

U = [initial_u(X)]

def u(x, t):
    uvals = []
    for j in range(len(x)):
        if j == 0:
            uvals.append(U[t - 1][j] + c * dt / (2 * dx) * (U[t - 1][j + 1] - U[t - 1][-1]))
        elif j == len(x) - 1:
            uvals.append(U[t - 1][j] + c * dt / (2 * dx) * (U[t - 1][0] - U[t - 1][j - 1]))
        else:
            uvals.append(U[t - 1][j] + c * dt / (2 * dx) * (U[t - 1][j + 1] - U[t - 1][j - 1]))
    return uvals

for t in range(1, 500):
    U.append(u(X, t))

plt.style.use('dark_background')
fig, ax = plt.subplots()
line, = ax.plot(X, U[0])

def update(frame):
    line.set_ydata(U[frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(500), blit=True)
plt.show()
