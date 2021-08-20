import numpy as np

def operations(a, b, k):
    c = 0
    if k == 0:
        c = a + b
    if k == 1:
        c = a - b
    if k == 2:
        c = b - a
    if k == 3:
        c = a * b
    if k == 4:
        if b != 0:
            c = a / b
    if k == 5:
        if a != 0:
            c = b / a
    return c 

def cal_24(x):
    c = 0
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
                                                c = 1
                                            
                                            r1 = operations(x[i], x[j], o1)
                                            r2 = operations(r1, x[m], o2)
                                            r = operations(r2, x[n], o3)
                                            if abs(r - 24) < 1e-12:
                                                c = 1
    return c

counts = 0
total = 0
k = 11
for i in range(1, k):
    for j in range(i, k):
        for m in range(j, k):
            for n in range(m, k):
                total = total + 1
                a = np.array([i,j,m,n])
                if cal_24(a) == 1:
                    counts = counts + 1

print(total,counts,total-counts)


def show_24(x):
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
                                                print("两个括号",i,j,m,n,o1,o2,o3)

                                            r1 = operations(x[i], x[j], o1)
                                            r2 = operations(r1, x[m], o2)
                                            r = operations(r2, x[n], o3)
                                            if abs(r - 24) < 1e-12:
                                                print("非两个括号",i,j,m,n,o1,o2,o3)

a = np.array([3,3,8,8])
show_24(a)

# 1~10 715种 566种成功 149种失败
# 2~10 J Q K A 1820种 1362种成功 458种失败