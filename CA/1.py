import random as random

a = [random.randint(0,1) for i in range(0,100)]

print(a)
print(len(a))

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

def print_str(a):
    a_s = ''
    for i in range(0, len(a)):
        if a[i] == 0:
            a_s = a_s + ' '
        if a[i] == 1:
            a_s = a_s + '@'
    print(a_s)

for i in range(0, 200):
    a = rule_22(a)
    print_str(a)