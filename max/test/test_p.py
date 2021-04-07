def all_permutation(a,i):
    a_c = a[:1]
    a_all = []
    i = int(i)
    for j in range(1, len(a)):
        n = len(a_c)
        a_c.append(a[j])

        for k in range(0, n):
            a_c.append(list([a_c[j]])+list([a[i]]))
    print("-1:",a_c[55:60])
    for j in range(0, len(a_c)):
        if len(a_c[j]) == i:
            a_all.append(a_c[j])
    return a_all

number = list(range(0,12)) # 产生每个选修课的标号为各种排列作准备
print(number)
for i in range(0,len(number)):
    number[i] = str(number[i])

print(number)
number_i = all_permutation(number,1)
print("number",number_i)