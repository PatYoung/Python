import os
import shutil

main = "1.exe"
#r_v = os.system(main) 
os.system(main) 
# print ("r_v:",r_v)
	
f = open("1.dat")
print("512:",f.read(512)) #读取512字节
print("512 stop") 
print("1024:",f.read(1024)) #读取1024字节
print("1024 stop") 


while True:
	lines = f.readline()
	# print("lines in while:",lines)
	if not lines:
		break
		
f.close()

with open('1.dat','r',encoding='utf-8') as f:
	lines = []
	i = 0
	for line in f.readlines():
		i = i + 1
		if line != '\n': #如果不是最后一行，将读取的存入
			lines.append(line)
			f.close()

# print ("lines out while:",lines)

with open('2.dat','w',encoding='utf-8') as f:
	lines[0] = '1 \n'
	for j in range(1,i+1):
		f.write('%s' %lines[j-1]) 

	
num = 11

for i in range(1,num):		
	a = os.getcwd() # 获取当前路径
	# print("%s%s" %(a,"\\1"))
	b = os.listdir() # 获取当前路径下所有文件名
	# print(b)
	c = os.path.exists("%s%s%d" %(a,"\\",i)) # 查看是否存在该路径，返回值未布尔函数值
	# print(c)
	
	if c == False:
		os.mkdir("%d" %(i)) # 创建新的路径
		shutil.copyfile("1.dat","%s%s%d\\2.dat" %(a,"\\",i)) # （在程序所在目录下）复制文件（文件名在前）到新路径（位置在后）
		os.rename("%s%s%d\\2.dat" %(a,"\\",i),"%s%s%d%s%d.dat" %(a,"\\",i,"\\",i)) # 改文件名
		
	#shutil.rmtree("%s%s%d" %(a,"\\",i))

	
a = os.getcwd()
print ("%s%s" %(a,"\\1"))