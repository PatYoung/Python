a = []
b = []
c = []
x = []
y = []
i = 0
j = 0
k = 0
n = 0
m = 0
s = 0
l = 0
p = 0
q = 0
n = input("How many lessons?")
while i < n :
    a.append(input("What is the grade?"))
    b.append(input("What is the weight?"))
    c.append(a[i]*b[i])
    print ""
    i = i + 1

s = sum(c)/sum(b)

print s

m = input("How many extra lessons?")
while j < m :
    x.append(input("What is the grade?"))
    y.append(input("What is the weight?"))
    print ""
    j = j + 1
l = s
while k < m :
    #if x[k] <= s :
    #    s = s + x[k] * y[k] * 0.002
    #else :
    p = s + x[k] * y[k] * 0.002
    l = l + x[k] * y[k] * 0.002
    q =(s * sum(b) + x[k] * y[k]) /(sum(b) + y[k])
    if p < q :
        s = q
    else :
        s = p
    k = k + 1

print "Driect add:",l
print "Max:",s
