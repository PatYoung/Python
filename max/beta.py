import numpy as np
import random

beta = 0.002

a_1 = [] # 必修课成绩
b_1 = [] # 必修课绩点

a_2 = [] # 选修课成绩
b_2 = [] # 选修课绩点

number = [] # 所有选修课的序号
number_i = [] # 储存选i个选修课的所有排列，且从小到大排列
number_i_j = [] # number_i中第j个

a_c = [] # 计算加权平均的中间成绩储存列表
b_c = [] # 计算加权平均的中间绩点储存列表

a_left = [] # 记录应在第二部分计算的选修课序号

result_0 = 0.0 # 存储必修课加权平均分
result_1 = 0.0 # 存储每一个中间的总成绩，并存入result中
result = [] # 储存上面中间值
result_class = [] # 储存计算出result加入的选修课
max_grade = 0
max_class = ''


##### 产生所有在列表a中选取i个元素排列的函数 #####
def all_permutation(a,i):
    a_c = a[:1]
    a_c = [a_c]
    a_all = []
    i = int(i)
    for j in range(1, len(a)):
        n = len(a_c)
        a_c.append([a[j]])
        for k in range(0, n):
            a_cc = a_c[k][:]
            a_cc.append(a[j])
            a_c.append(a_cc)

    for j in range(0, len(a_c)):
        if len(a_c[j]) == i:
            a_all.append(a_c[j])
    return a_all
#####

a_1 = [90]
b_1 = [20]

a_2 = [93, 92, 95, 94, 100, 96, 91, 100, 90, 93, 98, 100, 93]
b_2 = [3, 3, 2, 3, 3, 1, 4, 2, 4, 3, 4, 1, 3]

a_1 = int(random.randint(80, 90))
b_1 = int(random.randint(15, 20))
n = int(random.randint(1, 15))
a_2 = [random.randint(a_1,a_1+10) for i in range(1, n)]
b_2 = [random.randint(1,4) for i in range(1, n)]

a_1 = [a_1]
b_1 = [b_1]

a_1 = [90]
b_1 = [15]
a_2 = [99, 98, 98, 98, 98, 96, 94, 94, 93, 93, 92, 92, 90]
b_2 = [4, 4, 3, 3, 2, 3, 3, 1, 1, 2, 2, 2, 1]

print(a_1, b_1)
print(a_2)
print(b_2)

a_1 = np.array(a_1)
b_1 = np.array(b_1)

a_2 = np.array(a_2)
b_2 = np.array(b_2)

number = list(range(0,len(a_2))) # 产生每个选修课的标号为各种排列作准备
print("a:", number)
for i in range(0,len(number)):
    number[i] = str(number[i])

# 必修课平均值
result_0 = sum(a_1*b_1)/sum(b_1)

# 不加入选修课的成绩
result_1 = result_0 + beta*sum(a_2*b_2)
result.append(result_1)
result_class.append("")

for i in range(1,len(a_2)):
    number_i = all_permutation(number,i)
    # print(len(number_i))
    for j in range(0,len(number_i)):
        number_i_j = number_i[j]
        a_c = [result_0]
        b_c = [sum(b_1)]
        result_class.append(list(number_i_j))

        for k in range(0,len(number_i_j)):
            a_c.append(a_2[int(number_i_j[k])])
            b_c.append(b_2[int(number_i_j[k])])
        
        a_c = np.array(a_c)
        b_c = np.array(b_c)

        result_1 = sum(a_c*b_c)/sum(b_c)

        a_left = list(set(number) - set(number_i_j))
        for k in range(0, len(a_2)-i):
            result_1 = result_1 + beta*a_2[int(a_left[k])]*b_2[int(a_left[k])]

        result.append(result_1)

# 选修课全加入的成绩
result_1 = (sum(a_1*b_1)+sum(a_2*b_2))/(sum(b_1)+sum(b_2))
result.append(result_1)
result_class.append(number)

max_grade = max(result)
max_class = result_class[result.index(max(result))]

print("必修课平均值：", result_0)
print("最大可能的结果：", max(result))
ii = 0
for i in range(0, 2**len(a_2)):
    if abs((result[i] - max_grade)/max_grade) < 1e-15:
        ii = ii + 1
        max_class = result_class[i]
        print("\n第",ii,"种可能，可加入以下选修课：\n")
        for i in range(0, len(max_class)):
            print("第",int(max_class[i])+1,"门：","分数:",a_2[int(max_class[i])],"，绩点:",b_2[int(max_class[i])])

# print(result)
# print(result_class[result.index(max(result))])


print("############################")
print("以下为近似算法：")
####################################################################################################
### 一种近似算法，按“正”贡献排序
####################################################################################################
print("############################")
print("按“正”贡献排序:")
a = result_0
b = sum(b_1)
x = list(a_2)
y = list(b_2)

for i in range(0, len(x)):
    for j in range(i, len(x)):
        c_1 = (a*b+x[i]*y[i])/(b+y[i])-beta*x[i]*y[i]
        c_2 = (a*b+x[j]*y[j])/(b+y[j])-beta*x[j]*y[j]
        if c_1 < c_2:
            x_c = x[i]
            x[i] = x[j]
            x[j] = x_c
            y_c = y[i]
            y[i] = y[j]
            y[j] = y_c

print("b x",x)
print("b y",y)

cc_1 = a*b
cc_2 = b
cc_3 = 0.0
cc_4 = []
m = 0

for i in range(0, len(x)):
    cc_1 = a*b
    cc_2 = b
    for j in range(0, i+1):
        cc_1 = cc_1 + x[j]*y[j]
        cc_2 = cc_2 + y[j]
    cc_3 = 0.0
    for jj in range(i+1, len(x)):
        cc_3 = cc_3 + x[jj]*y[jj]
    cc_4.append(cc_1/cc_2+beta*cc_3)

# print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为最大，近似算得：", max(cc_4))
print("b x", x[0:cc_4.index(max(cc_4))+1])
print("b y", y[0:cc_4.index(max(cc_4))+1])
####################################################################################################
### 另一种近似算法，按成绩从大到小，相同成绩绩点从小到大排序
####################################################################################################
print("############################")
print("成绩从大到小，相同成绩绩点从小到大排序:")
a = result_0
b = sum(b_1)
x = list(a_2)
y = list(b_2)

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] < x[j]:
            x_c = x[i]
            x[i] = x[j]
            x[j] = x_c
            y_c = y[i]
            y[i] = y[j]
            y[j] = y_c  

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] == x[j]:
            if y[i] > y[j]:
                x_c = x[i]
                x[i] = x[j]
                x[j] = x_c
                y_c = y[i]
                y[i] = y[j]
                y[j] = y_c  

print("c x",x)
print("c y",y)

cc_4 = []

for i in range(0, len(x)):
    cc_1 = a*b
    cc_2 = b
    for j in range(0, i+1):
        cc_1 = cc_1 + x[j]*y[j]
        cc_2 = cc_2 + y[j]
    cc_3 = 0.0
    for jj in range(i+1, len(x)):
        cc_3 = cc_3 + x[jj]*y[jj]
    cc_4.append(cc_1/cc_2+beta*cc_3)

# print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为最大，近似算得：", max(cc_4))
print("c x", x[0:cc_4.index(max(cc_4))+1])
print("c y", y[0:cc_4.index(max(cc_4))+1])
####################################################################################################
### 另一种近似算法，按成绩从大到小，相同成绩绩点从大到小排序
####################################################################################################
print("############################")
print("按成绩从大到小，相同成绩绩点从大到小排序：")
a = result_0
b = sum(b_1)
x = list(a_2)
y = list(b_2)

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] < x[j]:
            x_c = x[i]
            x[i] = x[j]
            x[j] = x_c
            y_c = y[i]
            y[i] = y[j]
            y[j] = y_c  

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] == x[j]:
            if y[i] < y[j]:
                x_c = x[i]
                x[i] = x[j]
                x[j] = x_c
                y_c = y[i]
                y[i] = y[j]
                y[j] = y_c  

# print("d x",x)
# print("d y",y)

cc_4 = []

for i in range(0, len(x)):
    cc_1 = a*b
    cc_2 = b
    for j in range(0, i+1):
        cc_1 = cc_1 + x[j]*y[j]
        cc_2 = cc_2 + y[j]
    cc_3 = 0.0
    for jj in range(i+1, len(x)):
        cc_3 = cc_3 + x[jj]*y[jj]
    cc_4.append(cc_1/cc_2+beta*cc_3)

# print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为最大，近似算得：", max(cc_4))
print("d x", x[0:cc_4.index(max(cc_4))+1])
print("d y", y[0:cc_4.index(max(cc_4))+1])
####################################################################################################
### 另一种近似算法，一个一个加入当前最大贡献的
####################################################################################################
print("############################")
print("一个一个加入当前最大贡献的：")
a = result_0
b = sum(b_1)
x = list(a_2)
y = list(b_2)
x_1 = []
y_1 = []
cc_4 = []

while len(x) > 0:
    for i in range(0, len(x)):
        for j in range(i, len(x)):
            c_1 = (a*b+x[i]*y[i])/(b+y[i])-beta*x[i]*y[i]
            c_2 = (a*b+x[j]*y[j])/(b+y[j])-beta*x[j]*y[j]
            if c_1 > c_2:
                x_c = x[i]
                x[i] = x[j]
                x[j] = x_c
                y_c = y[i]
                y[i] = y[j]
                y[j] = y_c

    a = (a*b+x[-1]*y[-1])/(b+y[-1])
    b = b + y[-1]
    x_1.append(x[-1])
    y_1.append(y[-1])
    x.pop()
    y.pop()

    cc_3 = 0.0
    for jj in range(0, len(x)):
        cc_3 = cc_3 + x[jj]*y[jj]
    cc_4.append(a+beta*cc_3)

# print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为最大，近似算得：", max(cc_4))
print("f x", x_1[0:cc_4.index(max(cc_4))+1])
print("f y", y_1[0:cc_4.index(max(cc_4))+1])
####################################################################################################
### 另一种近似算法，在按分数大小排列基础上，考虑之前的更大成绩的加权值
####################################################################################################
print("############################")
print("按分数大小排列基础上，考虑之前的更大成绩的加权值：")
a = result_0
b = sum(b_1)
x = list(a_2)
y = list(b_2)

cc_4 = []

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] < x[j]:
            x_c = x[i]
            x[i] = x[j]
            x[j] = x_c
            y_c = y[i]
            y[i] = y[j]
            y[j] = y_c  

x_1 = x[:]
y_1 = y[:]

x_2 = []
y_2 = []

while len(x_1) > 0:
    x_2.append(x_1[0])
    n_rep = 0
    d_tot = 0
    for i in range(0, len(x_1)):
        if x_1[i] == x_1[0]:
            n_rep = n_rep + 1
            d_tot = d_tot + y_1[i]
    del x_1[0:n_rep]
    del y_1[0:n_rep]
    y_2.append(d_tot)

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] == x[j]:
            a = result_0
            b = sum(b_1)
            for k in range(0, x_2.index(x[i])):
                a = (a*b + x_2[k]*y_2[k])/(b + y_2[k])
                b = b + y_2[k]

            c_1 = (a*b+x[i]*y[i])/(b+y[i])-beta*x[i]*y[i]+beta*x[i]*y_2[x_2.index(x[i])]
            c_2 = (a*b+x[j]*y[j])/(b+y[j])-beta*x[j]*y[j]+beta*x[i]*y_2[x_2.index(x[i])]

            if c_1 < c_2:
                x_c = x[i]
                x[i] = x[j]
                x[j] = x_c
                y_c = y[i]
                y[i] = y[j]
                y[j] = y_c

#print("e x",x)
#print("e y",y)
a = result_0
b = sum(b_1)
for i in range(0, len(x)):
    cc_1 = a*b
    cc_2 = b
    for j in range(0, i+1):
        cc_1 = cc_1 + x[j]*y[j]
        cc_2 = cc_2 + y[j]
    cc_3 = 0.0
    for jj in range(i+1, len(x)):
        cc_3 = cc_3 + x[jj]*y[jj]
    cc_4.append(cc_1/cc_2+beta*cc_3)

# print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为最大，近似算得：", max(cc_4))
print("e x", x[0:cc_4.index(max(cc_4))+1])
print("e y", y[0:cc_4.index(max(cc_4))+1])
####################################################################################################
### 另一种近似算法，在按分数大小排列基础上，考虑之前的更大成绩的加权值，并计算之后m个相同成绩的2^(m)种可能，如果不是全是利用加权平均，截至
####################################################################################################
print("############################")
print("按分数大小排列基础上，考虑之前的更大成绩的加权值,并计算之后m个相同成绩的2^(m)种可能：")
a = result_0
b = sum(b_1)
x = list(a_2)
y = list(b_2)

cc_4 = []

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] < x[j]:
            x_c = x[i]
            x[i] = x[j]
            x[j] = x_c
            y_c = y[i]
            y[i] = y[j]
            y[j] = y_c  

# print("before")
# print(x)
# print(y)

x_1 = x[:]
y_1 = y[:]

x_2 = []
y_2 = []
n_r = []

x_c = []
y_c = []

while len(x_1) > 0:
    x_2.append(x_1[0])
    n_rep = 0
    d_tot = 0
    for i in range(0, len(x_1)):
        if x_1[i] == x_1[0]:
            n_rep = n_rep + 1
            d_tot = d_tot + y_1[i]
    del x_1[0:n_rep]
    del y_1[0:n_rep]
    y_2.append(d_tot)
    n_r.append(n_rep)

# print("number of rep",n_r)
# print("number of rep",x_2)
# print("number of rep",y_2)
ccc_max = []

for i in range(0, len(n_r)):
    ccc_1 = []
    ccc_2 = []
    if i > 0:
        a = (a*b + x_2[i-1]*y_2[i-1])/(b + y_2[i-1])
        b = b + y_2[i-1]
    

    for j in range(0, 2**(n_r[i])):
        bin_c = list(bin(j))
        del bin_c[0:2]

        while len(bin_c) < n_r[i]:
            bin_c.insert(0,'0')

        # print(j, bin_c)
        cccc_1 = a*b
        cccc_2 = b
        cccc_3 = 0
        for k in range(0, n_r[i]):
            if i == 0:
                cccc_1 = cccc_1 + int(bin_c[k])*x[k]*y[k]
                cccc_2 = cccc_2 + int(bin_c[k])*y[k]
                cccc_3 = cccc_3 + (1-int(bin_c[k]))*beta*x[k]*y[k]
            else:
                cccc_1 = cccc_1 + int(bin_c[k])*x[n_r[i-1]+k]*y[n_r[i-1]+k]
                cccc_2 = cccc_2 + int(bin_c[k])*y[n_r[i-1]+k]
                cccc_3 = cccc_3 + (1-int(bin_c[k]))*beta*x[n_r[i-1]+k]*y[n_r[i-1]+k]
        ccc_1.append(cccc_1/cccc_2+cccc_3)
        ccc_2.append(bin_c)
    
    # print(ccc_1)
    # print(ccc_2)
    # print(i,"max",ccc_1.index(max(ccc_1))+1)

    ccc_max = ccc_max + ccc_2[ccc_1.index(max(ccc_1))]
    if ccc_1.index(max(ccc_1))+1 != 2**(n_r[i]):
        break

while len(ccc_max) < len(x):
    ccc_max.append('0')

for i in range(0, len(ccc_max)):
    ccc_max[i] = int(ccc_max[i])

# print(x)
# print(y)
# print(ccc_max)

for i in range(0, len(x)):
    for j in range(i, len(x)):
        if x[i] == x[j]:
            if ccc_max[i] < ccc_max[j]:
                x_c = x[i]
                x[i] = x[j]
                x[j] = x_c
                y_c = y[i]
                y[i] = y[j]
                y[j] = y_c 
                ccc_max_c = ccc_max[i]
                ccc_max[i] = ccc_max[j]
                ccc_max[j] = ccc_max_c

# print(x)
# print(y)
# print(ccc_max)
a = result_0
b = sum(b_1)
for i in range(0, len(x)):
    cc_1 = a*b
    cc_2 = b
    for j in range(0, i+1):
        cc_1 = cc_1 + x[j]*y[j]
        cc_2 = cc_2 + y[j]
    cc_3 = 0.0
    for jj in range(i+1, len(x)):
        cc_3 = cc_3 + x[jj]*y[jj]
    cc_4.append(cc_1/cc_2+beta*cc_3)

# print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为最大，近似算得：", max(cc_4))
print("f x", x[0:cc_4.index(max(cc_4))+1])
print("f y", y[0:cc_4.index(max(cc_4))+1])
####################################################################################################
### 测试数据
####################################################################################################
# 一套测试数据
# [90] [15]
# [99, 99, 99, 98, 98, 98, 97, 97, 95, 93, 93, 92, 91]
# [1, 2, 3, 1, 3, 4, 1, 2, 3, 1, 4, 1, 3]

# 一套测试数据
# [87] [18]
# [89, 95, 95, 95, 91, 87, 96, 88, 89, 88, 94, 91, 91]
# [4, 3, 2, 4, 4, 1, 3, 2, 4, 3, 3, 4, 4] 

# 一套测试数据
# [85] [20]
# [88, 88]
# [2, 1]

# 一套测试数据
# [90] [15]
# [99, 98, 98, 98, 98, 96, 94, 94, 93, 93, 92, 92, 90]
# [4, 4, 3, 3, 2, 3, 3, 1, 1, 2, 2, 2, 1]

# 一套测试数据
# [81] [17]
# [89, 88, 88, 89, 88, 85, 84, 83, 83, 84, 83, 81, 82, 82]
# [3, 4, 2, 1, 1, 1, 2, 1, 1, 4, 3, 2, 3, 4]

# 一套测试数据
# [84] [17]
# [87, 89, 92, 84, 93, 85, 93, 85, 93, 93, 93, 88, 93, 87]
# [2, 2, 3, 2, 4, 4, 2, 4, 1, 4, 4, 3, 3, 2]