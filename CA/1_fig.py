import matplotlib.pyplot as plt
import random as random

def rule_22(a):
    rule = [0,0,0,1,0,1,1,0]
    acc = []
    acc[:] = a[:]
    for i in range(0, len(a)):
        ac = '' 
        for j in range(-1,2):
            n = i + j
            if n >= len(a):
                n = 0
                ac = ac + str(a[n])
            else:
                ac = ac + str(a[n])
        for k in range(0, len(rule)):
            if int(ac, 2) == k:
                acc[i] = rule[len(rule)-1-k]
    a[:] = acc[:]
    return a    

a = [random.randint(0,1) for i in range(0,200)]
# a[:] = [0 for i in range(0, 200)]
# a[0:10] = [1 for i in range(0, 10)]
# a[80:82] = [1 for i in range(8, 82)]
# a[100:138] = [1 for i in range(100, 138)]


plt.figure(figsize=(5,5))

for i in range(0, 200):
    a = rule_22(a)
    y = []
    x = []    
    for j in range(0, 200):
        if a[j] == 1:
            x.append(j/100)
            y.append(i/100)
    plt.scatter(x, y, s = 1, c = 'black', marker = 'o') 


plt.show()