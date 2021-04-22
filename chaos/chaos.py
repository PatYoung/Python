import numpy as np
import matplotlib.pyplot as plt

x_0 = 0.618

mu = np.arange(0.001, 2.001, 0.001)

for i in range(0, 2000):
    y = []
    mu_x = []
    x = x_0
    for j in range(0, 1000):
        x = 1 - mu[i]*x**2
        if j > 199:
            y.append(x)
            mu_x.append(mu[i])
    plt.scatter(mu_x, y, s=0.1, c='k', marker='.') 

plt.show()