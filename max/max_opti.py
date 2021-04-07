import random

a = int(random.randint(80, 90))
b = int(random.randint(15, 20))
k = 0.002
print(a, b)
n = int(random.randint(1, 15))
x = [random.randint(a,a+10) for i in range(1, n)]
y = [random.randint(1,4) for i in range(1, n)]
print(x)
print(y)

x_g = []
y_g = []

for i in range(1,11):
    print(i,a/(1-k*(b+i)))

c_0 = 0.0

for i in range(0, len(x)):
    c_0 = (a*b+x[i]*y[i])/(b+y[i])-a-k*x[i]*y[i]
    if c_0 > 0:
        x_g.append(x[i])
        y_g.append(y[i])
    

c_1 = 0.0
c_2 = 0.0
c = 0
m = 0
for i in range(0, len(x_g)):
    c_1 = (a*b+x_g[i]*y_g[i])/(b+y_g[i])-k*x_g[i]*y_g[i]
    for j in range(i+1, len(x_g)):
        c_2 = (a*b+x_g[j]*y_g[j])/(b+y_g[j])-k*x_g[j]*y_g[j]
        if c_1 < c_2:
            c = x_g[j]
            x_g[j] = x_g[i]
            x_g[i] = c
            c = y_g[j]
            y_g[j] = y_g[i]
            y_g[i] = c

for i in range(0, len(x_g)):
    c_1 = (a*b+x_g[i]*y_g[i])/(b+y_g[i])-k*x_g[i]*y_g[i]
    print(c_1)

print(x_g)
print(y_g)

cc_1 = a*b
cc_2 = b
cc_3 = 0.0
cc_4 = []

for i in range(0, len(x_g)):
    cc_1 = a*b
    cc_2 = b
    for j in range(0, i+1):
        cc_1 = cc_1 + x_g[j]*y_g[j]
        cc_2 = cc_2 + y_g[j]
    cc_3 = 0.0
    for jj in range(i+1, len(x_g)):
        cc_3 = cc_3 + x_g[jj]*y_g[jj]
    cc_4.append(cc_1/cc_2+k*cc_3)




if len(cc_4) != 0:
    m = cc_4.index(max(cc_4))
    print("m:",m)

    for i in range(0,m+1):
        print(x_g[i],y_g[i])




