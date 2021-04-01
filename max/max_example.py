a = []
b = []
c = []

a.append(88)
a.append(3)

b.append(89)
b.append(1)

c.append(90)
c.append(1)

print(a[0]*a[1])

m = list(range(0,4))

print(m)

m[0] = a[0] + 0.002*(b[0]*b[1]+c[0]*c[1])
m[1] = (a[0]*a[1]+b[0]*b[1])/(a[1]+b[1]) + 0.002*(c[0]*c[1])
m[2] = (a[0]*a[1]+c[0]*c[1])/(a[1]+c[1]) + 0.002*(b[0]*b[1])
m[3] = (a[0]*a[1]+b[0]*b[1]+c[0]*c[1])/(a[1]+b[1]+c[1])

print(m)