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

# 　　身份证号码的意义
# 　　①前1、2位数字表示：所在省份的代码，河南的省份代码是41哦!
# 　　②第3、4位数字表示：所在城市的代码;
# 　　③第5、6位数字表示：所在区县的代码;
# 　　④第7~14位数字表示：出生年、月、日;
# 　　⑤第15、16位数字表示：所在地的派出所的代码;
# 　　⑥第17位数字表示性别：奇数表示男性，偶数表示女性;
# 　　⑦第18位数字是校检码：也有的说是个人信息码，一般是随计算机随机产生，用来检验身份证的正确性。校检码可以是0~9的数字，有时也用x表示。