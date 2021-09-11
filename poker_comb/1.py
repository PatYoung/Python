import random as random
import math as math
import time as time

t_0 = time.time()

def counts_normal_bomb(a):
    bomb = 0
    bomb_i = 0
    for i in range(1,14):
        bomb_i = 0
        bomb_i = a.count(i)
        if bomb_i == 4:
            bomb = bomb + 1
    return bomb

def counts_special_bomb(a):
    bomb = 0
    if a.count(0) == 2:
        bomb = 1
    return bomb

rep = 10000000

a_0 = [i for i in range(1,14)]*4 + [0]*2
a = []

x_1 = 0
x_2 = 0
y_1 = 0
y_2 = 0
z_1 = 0
z_2 = 0
x_1_a = 0
y_1_a = 0
z_1_a = 0
x_2_a = 0
y_2_a = 0
z_2_a = 0

x_bomb_exist = 0
y_bomb_exist = 0
z_bomb_exist = 0
n_bomb_exist = 0

for i in range(0, rep):
    a[:] = a_0[:]

    random.shuffle(a) #随机打乱列表

    x = a[:17]
    y = a[17:34]
    z = a[34:]
    if counts_normal_bomb(x) != 0:
        x_1 = x_1 + 1
    if counts_normal_bomb(y) != 0:
        y_1 = y_1 + 1
    if counts_normal_bomb(z) != 0:
        z_1 = z_1 + 1

    x = a[:17]
    y = a[17:34]
    z = a[34:]
    x_2 = x_2 + counts_special_bomb(x)
    y_2 = y_2 + counts_special_bomb(y) 
    z_2 = z_2 + counts_special_bomb(z) 

    if counts_normal_bomb(x) != 0 and counts_special_bomb(x) == 0:
        x_1_a = x_1_a + 1
    if counts_normal_bomb(y) != 0 and counts_special_bomb(y) == 0:
        y_1_a = y_1_a + 1
    if counts_normal_bomb(z) != 0 and counts_special_bomb(z) == 0:
        z_1_a = z_1_a + 1

    if counts_normal_bomb(x) == 0 and counts_special_bomb(x) != 0:
        x_2_a = x_2_a + 1
    if counts_normal_bomb(y) == 0 and counts_special_bomb(y) != 0:
        y_2_a = y_2_a + 1
    if counts_normal_bomb(z) == 0 and counts_special_bomb(z) != 0:
        z_2_a = z_2_a + 1

    if counts_normal_bomb(x) != 0 or counts_special_bomb(x) != 0:
        x_bomb_exist = x_bomb_exist + 1
    if counts_normal_bomb(y) != 0 or counts_special_bomb(y) != 0:
        y_bomb_exist = y_bomb_exist + 1
    if counts_normal_bomb(z) != 0 or counts_special_bomb(z) != 0:
        z_bomb_exist = z_bomb_exist + 1                

    if counts_normal_bomb(x) + counts_special_bomb(x) + counts_normal_bomb(y) + counts_special_bomb(y) + counts_normal_bomb(z) + counts_special_bomb(z) != 0:
        n_bomb_exist = n_bomb_exist + 1

# A_i 表示拿到4个i的炸弹（不含王炸）
# 至少拿一个普通炸弹概率为
# P(A_1∪A_2∪A_3∪...∪A_13) = Σ_i P(A_i) - Σ_ij P(A_i A_j) + Σ_ijk P(A_i A_j A_k) - ... （容斥恒等式）

# 至少拿到一个普通炸弹概率为（包含能拿到王炸可能）
def cal_p_normal(n):
    p = 0
    for i in range(1,14):
        if 4*i < n:
            p = p + (-1)**(i+1)*math.comb(13,i)*math.comb(n,4*i)/math.comb(54,4*i)
    return p

# 拿到王炸概率为（包含能拿到普通炸弹可能）
def cal_p_special(n):
    p = math.comb(52,n-2)/math.comb(54,n)
    return p

# 至少拿到一个普通炸弹概率为（不包含能拿到王炸可能）
def cal_p_normal_alone(n):
    p = 0
    for i in range(1,14):
        if 4*i < n:
            p = p + (-1)**(i+1)*math.comb(13,i)*(math.comb(n,4*i)/math.comb(54,4*i)-math.comb(n,4*i+2)/math.comb(54,4*i+2))
    return p


# 此处事件为 B_i 表示拿到4个i的炸弹和王炸，利用容斥恒等式计算
# 同时拿到普通炸弹和王炸概率为
def cal_p_normal_2(n):
    p = 0
    for i in range(1,14):
        if 4*i < n:
            p = p + (-1)**(i+1)*math.comb(13,i)*math.comb(n,4*i+2)/math.comb(54,4*i+2)
    return p

# 仅拿到王炸概率，即，拿到王炸概率（含普通炸弹）- 同时拿到普通炸弹和王炸概率
def cal_p_special_alone(n):
    p = math.comb(52,n-2)/math.comb(54,n) - cal_p_normal_2(n)
    return p

print(x_1/rep, y_1/rep, z_1/rep)
print(x_2/rep, y_2/rep, z_2/rep)

print(x_1_a/rep,y_1_a/rep,z_1_a/rep)
print(x_2_a/rep,y_2_a/rep,z_2_a/rep)

print(cal_p_normal(17), cal_p_normal(20))
print(cal_p_special(17), cal_p_special(20))

print(cal_p_normal_alone(17), cal_p_normal_alone(20))
print(cal_p_special_alone(17), cal_p_special_alone(20))
print("xyz")
print(x_bomb_exist/rep, y_bomb_exist/rep, z_bomb_exist/rep)

x = cal_p_normal(17) + cal_p_special(17) - cal_p_normal_2(17) # 至少拿一个炸弹（任意）
y = cal_p_normal(17) + cal_p_special(17) - cal_p_normal_2(17) # 至少拿一个炸弹（任意）
z = cal_p_normal(20) + cal_p_special(20) - cal_p_normal_2(20) # 至少拿一个炸弹（任意）
print("xyz")
print(x, y, z)

print(n_bomb_exist/rep)

p_bomb_exist = x + y + z

def cal_p_double_normal(n):
    p = 0
    for i in range(1,14):
        if 4*i < n:
            p = p + (-1)**(i+1)*math.comb(13,i)*math.comb(n,4*i)/math.comb(54,4*i)
    return p   

xy = 2*cal_p_special(17)*cal_p_normal_alone(17) + cal_p_normal_alone(17)*cal_p_normal_alone(17)
xz = cal_p_special(17)*cal_p_normal_alone(20) + cal_p_special(20)*cal_p_normal_alone(17) + cal_p_normal_alone(20)*cal_p_normal_alone(17)
yz = cal_p_special(17)*cal_p_normal_alone(20) + cal_p_special(20)*cal_p_normal_alone(17) + cal_p_normal_alone(20)*cal_p_normal_alone(17)

p_bomb_exist = p_bomb_exist - xy - xz - yz

xyz = 2*cal_p_special(17)*cal_p_normal_alone(17)*cal_p_normal_alone(20) + cal_p_special(20)*cal_p_normal_alone(17)*cal_p_normal_alone(17) + cal_p_normal_alone(20)*cal_p_normal_alone(17)*cal_p_normal_alone(20)

p_bomb_exist = p_bomb_exist + xyz

print(p_bomb_exist)

t_1 = time.time()
print(t_1-t_0)

# 0.1847787 0.1849934 0.3040512
# 0.5447697

# xyz
# 0.1848032 0.1847536 0.3035377
# xyz
# 0.18488876168923066 0.18488876168923066 0.30368614919177234 # 至少有一个炸弹解析解

# 100000000 次重复

# 普通炸弹
# 0.0960109
# 0.09599854 农民（17张牌）至少拿到一个普通炸弹概率（包含能拿到王炸可能）
# 0.18982805 地主（20张牌）至少拿到一个普通炸弹概率（包含能拿到王炸可能）

# 王炸
# 0.09508047 
# 0.09505693 农民（17张牌）拿到一个王炸概率（包含能拿到普通炸弹可能可能）
# 0.13277468 地主（20张牌）拿到一个王炸概率（包含能拿到普通炸弹可能可能）

# 仅普通炸弹
# 0.08984429 农民（17张牌）至少拿到一个普通炸弹概率（不包含能拿到王炸可能）

# 仅王炸
# 0.08891386 农民（17张牌）拿到一个王炸概率（不包含能拿到普通炸弹可能可能）

# 解析解
# 0.09601640795551145 农民（17张牌）至少拿到一个普通炸弹概率（包含能拿到王炸可能）
# 0.18982277497525848 地主（20张牌）至少拿到一个普通炸弹概率（包含能拿到王炸可能）
# 0.09503843466107617 农民（17张牌）拿到一个王炸概率（包含能拿到普通炸弹可能可能）
# 0.13277428371767994 地主（20张牌）拿到一个王炸概率（包含能拿到普通炸弹可能可能）

# 0.0898503270281545 农民（17张牌）至少拿到一个普通炸弹概率（不包含能拿到王炸可能）
# 0.17091186547409243 地主（20张牌）至少拿到一个普通炸弹概率（不包含能拿到王炸可能）
# 0.08887235373371921 农民（17张牌）拿到一个王炸概率（不包含能拿到普通炸弹可能可能）
# 0.11386337421651387 地主（20张牌）拿到一个王炸概率（不包含能拿到普通炸弹可能可能）