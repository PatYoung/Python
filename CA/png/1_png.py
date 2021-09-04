import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random as random

def rule_22(a):
    rule = [0,0,0,1,0,1,1,0]
    acc = []
    acc[:] = a[:]
    for i in range(0, len(a)):
        ac = '' 
        for j in range(-1,2):
            n = i + j
            if n >= len(a):
                n = 0
                ac = ac + str(a[n])
            else:
                ac = ac + str(a[n])
        for k in range(0, len(rule)):
            if int(ac, 2) == k:
                acc[i] = rule[len(rule)-1-k]
    a[:] = acc[:]
    return a    

a = [random.randint(0,1) for i in range(0,200)]

current_address = os.getcwd() #是当前打开终端的位置
current_list = os.listdir()
png_name = ""

print(current_address)
print(current_list)

for i in current_list:
    if "png" in i:
        png_name = i

print(png_name)

print("%s%s%s" %(current_address,"\\",png_name))
img = mpimg.imread("%s%s%s" %(current_address,"\\",png_name))

print(img.ndim)
print(len(img))
print(len(img[0]))
print(img[1,1])

for i in range(0, 200):
    a = rule_22(a)
    y = []
    x = []    
    for j in range(0, 200):
        if a[j] == 1:
            img[i,j] = [0., 0., 0.]

plt.imshow(img)
plt.show()