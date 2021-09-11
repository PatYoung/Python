# Lagrange Interpolation

import math as math
import matplotlib.pyplot as plt

x = []
y = []
k = 5
n = 16
for i in range(0, n):
    x.append(k)
    y.append(math.sin(k**2))
    k = k + (10-5)/n

plt.figure(figsize=[15,5])

plt.scatter(x,y,marker='o') # marker='x'

x_1 = []
y_1 = []

def lagrange_interpolation(x,y,x_0):
    y_0 = 0
    for i in range(0, len(y)):
        la_i = 1
        for j in range(0, len(x)):
            if j != i:
                la_i = la_i*(x_0-x[j])/(x[i]-x[j])
        y_0 = y_0 + la_i*y[i]
    return y_0 

k = x[0]
n = 50
for i in range(0,n+1):
    x_1.append(k)
    y_1.append(lagrange_interpolation(x,y,k))
    k = k + (x[-1]-x[0])/n

plt.scatter(x_1,y_1,marker='*')

x = []
y = []
k = 5
n = 500
for i in range(0, n):
    x.append(k)
    y.append(math.sin(k**2))
    k = k + (10-5)/n

plt.plot(x,y)

x = []
y = []
k = 5
n = 16
for i in range(0, n):
    x.append(k)
    y.append(math.log(k**2))
    k = k + (10-5)/n

plt.figure(figsize=[15,5])

plt.scatter(x,y,marker='o') # marker='x'

x_1 = []
y_1 = []

def lagrange_interpolation(x,y,x_0):
    y_0 = 0
    for i in range(0, len(y)):
        la_i = 1
        for j in range(0, len(x)):
            if j != i:
                la_i = la_i*(x_0-x[j])/(x[i]-x[j])
        y_0 = y_0 + la_i*y[i]
    return y_0 

k = x[0]
n = 50
for i in range(0,n+1):
    x_1.append(k)
    y_1.append(lagrange_interpolation(x,y,k))
    k = k + (x[-1]-x[0])/n

plt.scatter(x_1,y_1,marker='*')

x = []
y = []
k = 5
n = 500
for i in range(0, n):
    x.append(k)
    y.append(math.log(k**2))
    k = k + (10-5)/n

plt.plot(x,y)

plt.show()