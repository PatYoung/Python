import math as math
import random as random
import numpy as np

print(math.pi)

a = random.randint(2,10)
a0 = random.randint(1,a)
print(a,a0)
for i in range(0,10):
    a0 = (a0 + a/a0)/2
    print(i,a0,abs(a0-math.sqrt(a)))

b = np.array([random.randint(1,10) for i in range(0,10)])
print(b)
print(b[0:5])