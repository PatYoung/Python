import psutil
import matplotlib.pyplot as pl
import numpy as np
import time

i = 0
#j = 0
x = []
y = []
pl.axis([0, 100, 0, 100])
pl.ion()
for i in range(0, 100, 1):
    #time.sleep(0.01)
    x.append(i)
    y.append(psutil.cpu_percent())
    #pl.figure(1)
    pl.plot(x, y, color='green', alpha=0.5, label='cpu_userage')
    pl.pause(0.1)
pl.show()
