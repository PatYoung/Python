import matplotlib.pyplot as plt
import numpy as np 
import math as math

plt.figure(figsize=(10,10))

r = 8

x = []
y = []

x = [r*math.cos(a) for a in np.arange(0, 2*math.pi, 0.01)]
y = [r*math.sin(a) for a in np.arange(0, 2*math.pi, 0.01)]

plt.plot(x,y)

x_0 = 6
y_0 = 0

for a in np.arange(0, 2*math.pi, 0.05):
    x_1 = r*math.cos(a)
    y_1 = r*math.sin(a)
    x_2 = (x_0 + x_1)/2
    y_2 = (y_0 + y_1)/2
    if (y_1-y_0) != 0:
        k = -(x_1-x_0)/(y_1-y_0)
        x = [] 
        y = []
        for b in np.arange(-r, r, 0.05):
            x_3 = b 
            y_3 = k*(b - x_2) + y_2
            if x_3**2 + y_3**2 < r**2:
                x.append(x_3)
                y.append(y_3)
        plt.plot(x,y)
    if (y_1-y_0) == 0:
        x = [] 
        y = []
        for b in np.arange(-r, r, 0.05):
            x_3 = x_2 
            y_3 = b 
            if x_3**2 + y_3**2 < r**2:
                x.append(x_3)
                y.append(y_3)
        plt.plot(x,y)

x = [0,x_0]
y = [0,y_0]    
plt.scatter(x,y,marker='o')

plt.show()

