import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import average

m_earth = 5.9724e24 #(kg)
m_mars = 6.4171e23 #(kg)
m_sun = 1.988435e30 #(kg)

one_min = 60

g_constant = 6.67430e-11 #(s-2 m3 kg-1)

v_light = 299792458 #(m s-1) in vacuum(exact)

a_earth = 1.49596e11 #(m) semimajor axis of earth
a_mars = 2.27923e11 #(m) semimajor axis of mars
c_sun = 25e5



v_earth_min = 29.29e3 #(m s-1) min. orbital velocity
v_earth_max = 30.29e3 #(m s-1) max. orbital velocity
v_mars_0 = 0 #(km s-1)

# print(a_earth-c_sun,a_earth+c_sun)

x_sun = -c_sun/a_earth
y_sun = 0.0/a_earth

x_1 = []
y_1 = []
v_1 = []

delta_t = 0.1

x_1.append(a_earth/a_earth)
y_1.append(0/a_earth)

v_1_x = 0.0
v_1_y = v_earth_min

v_1.append((v_1_x**2+v_1_y**2)**(0.5))

acc_1 = 0

tot_time = int(60*60*24*3650)

for i in range(0, tot_time):
    acc_1 = g_constant*m_sun/((x_1[-1]-x_sun)**2 + (y_1[-1]-y_sun)**2)/a_earth**2
    v_1_x = v_1_x - acc_1*delta_t*x_1[-1]/(x_1[-1]**2 + y_1[-1]**2)
    v_1_y = v_1_y - acc_1*delta_t*y_1[-1]/(x_1[-1]**2 + y_1[-1]**2)
    # v_1.append((v_1_x**2+v_1_y**2)**(0.5))
    x_1.append(x_1[-1] + v_1_x*delta_t/a_earth)
    y_1.append(y_1[-1] + v_1_y*delta_t/a_earth)
    if abs(x_1[-1]**2 + y_1[-1]**2) < 1e-8:
        print(i)
        break

plt.plot(x_1,y_1)
plt.show()

# print(min(v_1)/one_min,max(v_1)/one_min)
