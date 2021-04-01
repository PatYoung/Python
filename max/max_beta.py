import numpy as np

n_1 = 0
a_1 = []
b_1 = []
m_2 = 0
a_2 = []
b_2 = []
a = []
b = []
c = []
a_c = []
b_c = []
a_set = {}
b_set = {}

result_0 = 0.0
result_1 = 0.0
result = []
result_class = []
max_grade = 0
max_class = ''

n_1 = int(input("必修课数目:\n"))
for i in range(0,n_1):
    a_1.append(int(input("第%d门分数：\n" % (i+1))))
    b_1.append(int(input("第%d门绩点：\n" % (i+1))))

n_2 = int(input("选修课数目：\n"))
for i in range(0,n_2):
    a_2.append(int(input("第%d门分数：\n" % (i+1))))
    b_2.append(int(input("第%d门绩点：\n" % (i+1))))


a_1 = np.array(a_1)
b_1 = np.array(b_1)

a_2 = np.array(a_2)
b_2 = np.array(b_2)

result_0 = sum(a_1*b_1)/sum(b_1)

print("必修课平均值：", result_0)

def all_permutation(a,i):
    b = a[:1]
    c = []
    i = int(i)
    for j in range(1, len(a)):
        n = len(b)
        b.append(a[j])
        for k in range(0, n):
            b.append(list(b[k])+list(a[j]))

    for j in range(0, len(b)):
        if len(b[j]) == i:
            c.append(b[j])
    return c

# result_0 = sum(a_1*b_1)/sum(b_1)

result_1 = result_0 + 0.002*sum(a_2*b_2)
result.append(result_1)
result_class.append("")

a = list(range(0,n_2))
for i in range(0,len(a)):
    a[i] = str(a[i])

for i in range(1,n_2):
    b = np.array(all_permutation(a,i))

    for j in range(0,len(b)):
        c = b[j]
        a_c = list(a_1[:])
        b_c = list(b_1[:])
        result_class.append(list(c))
        for k in range(0,len(c)):
            a_c.append(a_2[int(c[k])])
            b_c.append(b_2[int(c[k])])
        
        a_set = set(a) - set(c)
        a_set = list(a_set)
        a_c = np.array(a_c)
        b_c = np.array(b_c)

        result_1 = sum(a_c*b_c)/sum(b_c)

        for k in range(0, n_2-i):
            result_1 = result_1 + 0.002*a_2[int(a_set[k])]*b_2[int(a_set[k])]

        result.append(result_1)

result_1 = (sum(a_1*b_1)+sum(a_2*b_2))/(sum(b_1)+sum(b_2))
result.append(result_1)
result_class.append(a)
print(result)
print(result_class)

print(max(result))
print(result_class[result.index(max(result))])

max_grade = max(result)
max_class = result_class[result.index(max(result))]
print("可加入以下选修课：")
for i in range(0, len(max_class)):
    print("第",int(max_class[i])+1,"门：","分数:",a_2[int(max_class[i])],"，绩点:",b_2[int(max_class[i])])

