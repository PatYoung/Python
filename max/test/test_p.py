def all_permutation(a,i):
    a_c = a[:1]
    a_c = [a_c]
    print("a_c",a_c)
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

number = list(range(0,11)) # 产生每个选修课的标号为各种排列作准备
print(number)
for i in range(0,len(number)):
    number[i] = str(number[i])

print(number)
number_i = all_permutation(number,1)
print("number",number_i,len(number_i))