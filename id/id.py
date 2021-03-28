id_list = []
weight = []
corr = []
sum_id = 0
id = ""
judge_1 = True

id = input("Input your ID number:\n")
while len(id) != 18:
    print("Wrong! Input again:")
    id = input()
    
# print(type(id))

def check_type(x):
    try:
        int(x)
        return True
    except ValueError:
        pass
    return False


id_list = list(id)
# print(id_list)
for i in range(0,len(id_list)-1):
    judge_1 = check_type(id_list[i])
    if judge_1 == False:
        print("This is not a valid number. Run again.")
        exit()
    
weight = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
corr = [1,0,"X",9,8,7,6,5,4,3,2]

for i in range(0,len(weight)):
    sum_id = sum_id + weight[i]*int(id_list[i])

print(str(corr[sum_id%11]))
print(str(corr[sum_id%11]) == id_list[-1].title())

# 372522197308072610
# 37252219510513072x
# 372522197502010739
# 以上测试ID来源于
# (http://liaocheng.dzwww.com/lcxw/202009/t20200915_6607808.htm)

# 3a2522197308072610