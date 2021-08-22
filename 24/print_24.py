import numpy as np

def operations(a, b, o):
    c = 0
    if o == 0:
        c = a + b
    if o == 1:
        c = a - b
    if o == 2:
        c = b - a
    if o == 3:
        c = a * b
    if o == 4:
        if b != 0:
            c = a / b
    if o == 5:
        if a != 0:
            c = b / a
    return c 

def judge_print(a, b, o):
    c = 0
    if o%3 == 2:
        c = a
        a = b
        b = c
    if o == 0:
        s = "(%s+%s)" % (a,b)
    if o == 1 or o == 2:
        s = "(%s-%s)" % (a,b)
    if o == 3:
        s = "(%s*%s)" % (a,b)
    if o == 4 or o == 5:
        s = "(%s/%s)" % (a,b)
    return s

def print_24(x):
    for i in range(0,4):
        for j in range(0,4):
            if i != j:
                for m in range(0,4):
                    if m != i and m != j:
                        for n in range(0,4):
                            if n != i and n != j and n != m:
                                for o1 in range(0,6):
                                    for o2 in range(0,6):
                                        for o3 in range(0,6):
                                            r1 = operations(x[i], x[j], o1)
                                            r2 = operations(x[m], x[n], o2)
                                            r = operations(r1, r2, o3)
                                            if abs(r - 24) < 1e-12:
                                                s1 = judge_print(str(x[i]), str(x[j]), o1)
                                                s2 = judge_print(str(x[m]), str(x[n]), o2)
                                                print(judge_print(s1, s2, o3))

                                            r1 = operations(x[i], x[j], o1)
                                            r2 = operations(r1, x[m], o2)
                                            r = operations(r2, x[n], o3)
                                            if abs(r - 24) < 1e-12:
                                                s1 = judge_print(str(x[i]), str(x[j]), o1)
                                                s2 = judge_print(s1, str(x[m]), o2)
                                                print(judge_print(s2, str(x[n]), o3))

a = np.array([3,3,8,8])
print_24(a)

a = np.array([7,7,5,10])
print_24(a)

a = np.array([1,1,4,7])
print_24(a)