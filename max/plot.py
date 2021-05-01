from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

a = 90
b = 15
k = 0.002

print(a,b)

a = a*b + 99*4
b = b + 4
a = a/b

a_1 = 100
b_1 = 1

x = []
y = []
y_2 = []
y_3 = []

for i in np.arange(0, 300, 1):
    x.append(i)
    y_2.append((a*b+i*a_1)/(b+i)-k*i*a_1)
    y_3.append(i/(b+i)-k*i)

#plt.plot(x,y)

#plt.plot(x,y_2)

plt.plot(x,y_3)

plt.show()

print(sqrt(b*(a_1-a)/k/a_1)-b)
    