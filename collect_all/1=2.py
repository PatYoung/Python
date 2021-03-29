import math

x = 0.0
y = 0.0
a = 0.0

def c_k_n(k,n):
    x = math.factorial(n)/math.factorial(k)/math.factorial(n-k)
    x = int(x)
    return x

def cal_x(m,n):
    x = 0.0
    x = (1-1/m)**(n-1)
    return x

def cal_x_simple(m,n):
    x = 0
    x = (m-1)**(n-1)
    return x


def cal_y(m,n):
    y = 0.0
    a = 0.0
    for k in range(1,m):
        a = (1-(k+1)/m)**(n-1)+k/m*(1-k/m)**(n-2)
        y = y + a*c_k_n(k,m-1)*(-1)**(k+1)
    return y

def cal_y_simple(m,n):
    y = 0
    a = 0
    a_1 = []
    a_2 = []
    for k in range(1,m):
        a_1.append((m-k-1)**(n-1)*c_k_n(k,m-1)*(-1)**(k+1))
        a_2.append(k*(m-k)**(n-2)*c_k_n(k,m-1)*(-1)**(k+1))
        a = a_1[k-1]+a_2[k-1]
        y = y + a
        print(k,y)
    print(a_1)
    print(a_2)
    return y

print("n need to >1")

for m in range(1,11):
    for n in range(1,11):
        x = cal_x(m,n)
        y = cal_y(m,n)
        print("m,n,x,y",m,n,x-y)
m = 10
n = 20
print(cal_y_simple(m,n))
