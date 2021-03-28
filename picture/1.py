import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
a=np.array([0.1,0.2,0.3,
         0.4,0.5,0.6,
         0.7,0.8,0.9]).reshape(3,3)

b = os.getcwd() #是当前打开终端的位置
c = os.listdir()
d = ""

for i in c:
    if "png" in i:
        d = i
    
print("%s%s%s" %(b,"\\",d))
img = mpimg.imread("%s%s%s" %(b,"\\",d))

print(img.ndim)
print(len(img))
print(len(img[0]))
print(img[1,1])

img2 = np.array([[[1., 1., 1., 1.] for i in range(100)] for i in range(100)]).reshape(100,100,4)


i = 1
while i < 50:
    i = i + 1
    j = 0
    while j < 49:
        img2[i,i + j] = [0.01*j,0.005*j,0.003*j,0.02*j]
        j = j + 1

plt.imshow(img2)
#plt.imshow(img3)
plt.show() 