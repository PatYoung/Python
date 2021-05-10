import numpy as np
import matplotlib.pyplot as plt

dx = 0.01
x_1 = -10
x_2 = abs(x_1)+dx
x = np.arange(x_1, x_2, dx)

for i in range(0,1):

    width = 5/(i+1)
    wave_number = 2

    y = np.real((1/(np.pi**(0.25)*width**(0.5)))*np.exp((1j)*wave_number*x-x**2/(2*width**2)))
    
    plt.plot(x,y)

y = np.real((1/(np.pi**(0.25)*width**(0.5)))*np.exp(-x**2/(2*width**2)))
    
plt.plot(x,y)

y = -np.real((1/(np.pi**(0.25)*width**(0.5)))*np.exp(-x**2/(2*width**2)))
    
plt.plot(x,y)

y = 0.5*np.real((1/(np.pi**(0.25)*width**(0.5))))*x**0  
plt.plot(x,y)

# 2 sqrt(2 ln(2)) width => 半高全宽

x_2 = []
y_2 = []
for i in np.arange(-0.5, 0.6, 0.1):
    x_2.append((2*np.log(2))**(0.5)*width)
    y_2.append(i)

plt.plot(x_2,y_2)

plt.show()
