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

# print(result)

print("必修课平均值：", result_0)
print("最大可能的结果：", max(result))
# print(result_class[result.index(max(result))])
print("可加入以下选修课：")
for i in range(0, len(max_class)):
    print("第",int(max_class[i])+1,"门：","分数:",a_2[int(max_class[i])],"，绩点:",b_2[int(max_class[i])])

####################################################################################################
### 一种近似算法，按“正”贡献排序
####################################################################################################
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

print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为")
print("近似算得：", max(cc_4))

####################################################################################################
### 另一种近似算法，按成绩从大到小，相同成绩绩点从小到大排序
####################################################################################################

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

print(cc_4)
print("第", cc_4.index(max(cc_4))+1, "为")
print("近似算得：", max(cc_4))

# 一套测试数据
# [90] [15]
# [99, 99, 99, 98, 98, 98, 97, 97, 95, 93, 93, 92, 91]
# [1, 2, 3, 1, 3, 4, 1, 2, 3, 1, 4, 1, 3]

# 一套测试数据
# [87] [18]
# [89, 95, 95, 95, 91, 87, 96, 88, 89, 88, 94, 91, 91]
# [4, 3, 2, 4, 4, 1, 3, 2, 4, 3, 3, 4, 4] 
