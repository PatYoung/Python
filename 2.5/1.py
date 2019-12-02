import numpy as np 

m = 1
n = 401
a = [1,2,3,4]
print(a)

for i in range(1,n):
    m = m + 1
    a = [1,2,3,4]
    b = np.random.choice(a, size = None, replace = True, p = None)
    #print(b)
    bc = 0
    ac = a
    bc = np.random.choice(ac, size = None, replace = True, p = None)
    #print(i,b,a)
    #print(ac,a)
    while (bc != b):
        m = m + 1
        ac.remove(bc)
        #print(ac)
        bc = np.random.choice(ac, size = None, replace = True, p = None)
        #print (bc)

print(m)
print(m/(n-1.0))