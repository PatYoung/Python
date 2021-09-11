a = 2

a_0 = 1

for i in range(0,10):
    a_1 = a/a_0
    a_0 = (a_0+a_1)/2
    print(i, a_0)

a_0 = 1

for i in range(0,10):
    a_1 = a/a_0**2
    a_0 = (a_0+a_1)/2
    print(i, a_0)

a_0 = 1

for i in range(0,10):
    a_1 = a/a_0**4
    a_0 = (a_0+a_1)/2
    print(i, a_0)


print(a**0.5,a**(1/3),a**(1/5))