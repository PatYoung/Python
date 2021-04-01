a = ["a", "b", "c", "d"]

print(a)

b = a[:1]
print(b)

for i in range(1, len(a)):
    n = len(b)
    b.append(a[i])
    print(b)
    for j in range(0, n):
        b.append(list(b[j])+list(a[i]))
        print(b)

for i in range(0, len(a)+1):
    c = 0
    if i == 0:
        c = 1
    for j in range(0, len(b)):
        if len(b[j]) == i:
            c = c + 1
    print("c_",len(a),"^",i,"=",c)