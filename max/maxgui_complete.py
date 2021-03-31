import easygui as g
import numpy as np

a_1 = []
b_1 = []
a_1_tot = 0
b_1_tot = 0

a_2 = []
b_2 = []
a_add = []
b_add = []
add_count = 0

ave_1 = 0
ave_direct = 0
ave_max = 0

n = 0
m = 0
max_g = 0

msg = "最大绩点（整数，最小为1）"
title = "最大绩点"
fieldNames = ["输入"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg, title, fieldNames)
max_g = int(fieldValues[0])

msg = "必修课"
title = "必修课数目"
fieldNames = ["输入数目"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg, title, fieldNames)
n = int(fieldValues[0])

for i in range(0,n):
    msg = "必修课%d-输入分数" % (i+1)
    title = "必修课：分数"
    fieldNames = ["分数"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = g.multenterbox(msg, title, fieldNames)
    a_1.append(int(fieldValues[0]))
    msg_2 = "必修课%d-选择绩点" % (i+1)
    title_2 = "必修课：绩点"
    choices = list(range(1,max_g+1))
    if max_g != 1:
        choice = g.choicebox(msg_2, title_2, choices)
        b_1.append(int(choice))
    else:
        b_1.append(1)


a_1_tot = sum(np.array(a_1)*np.array(b_1))
b_1_tot = sum(np.array(b_1))
# print(a_1_tot,b_1_tot)
ave_1 =  a_1_tot/b_1_tot

msg = "选修课"
title = "选修课数目"
fieldNames = ["数目"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg, title, fieldNames)
m = int(fieldValues[0])

for i in range(0,m):
    msg = "选修课%d-输入分数:" % (i+1)
    title = "选修课：分数"
    fieldNames = ["分数"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = g.multenterbox(msg, title, fieldNames)
    a_2.append(int(fieldValues[0]))
    msg_2 = "选修课%d-选择绩点" % (i+1)
    title_2 = "绩点"
    choices = list(range(1,max_g+1))
    if max_g != 1:
        choice = g.choicebox(msg_2, title_2, choices)
        b_2.append(int(choice))
    else:
        b_2.append(1) 

# ave_direct = sum(np.array(a_1+a_2))/sum(np.array(b_1+b_2))

ave_direct = ave_1 + 0.002*sum(np.array(a_2)*np.array(b_2))

# print(ave_direct)

ave_max = ave_1

for i in range(0,m):
    p = ave_max + a_2[i] * b_2[i] * 0.002
    q = (a_1_tot + a_2[i] * b_2[i]) /(b_1_tot + b_2[i])
    if p < q:
        ave_max = q
        a_add.append(a_2[i])
        b_add.append(b_2[i])
        add_count = add_count + 1
    else:
        ave_max = p

g.msgbox("必修课平均分： %.3f \n选修课直接加： %.3f \n最大可能： %.3f"% (ave_1,ave_direct,ave_max), title = "结果", ok_button = "显示方案")

if add_count != 0:
    for i in range(0,add_count-1):
        g.msgbox("应加入该选修课 \n %d \n %d" % (a_add[i],b_add[i]), title = "方案", ok_button = "下一个")
    g.msgbox("应加入该选修课 \n %d \n %d" % (a_add[-1],b_add[-1]), title = "方案", ok_button = "OK")
else:
    g.msgbox("没有应加入的选修课", title = "方案", ok_button = "OK")
