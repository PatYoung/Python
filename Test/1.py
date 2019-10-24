import os
import shutil

main = "1.exe"
r_v = os.system(main) 
#print (r_v)
	
f = open("1.dat")
print(f.read(512)) 

while True:
	lines = f.readline()
	#print(lines)
	if not lines:
		break
		pass
		
f.close()

with open('1.dat','r',encoding='utf-8') as f:
	lines = []
	i = 0
	for line in f.readlines():
		i = i + 1
		if line!='\n':
			lines.append(line)
			f.close()

#print (lines)

with open('2.dat','w',encoding='utf-8') as f:
	lines[0] = '1 \n'
	for j in range(1,i+1):
		f.write('%s' %lines[j-1]) 

	
num = 11

for i in range(1,num):		
	a = os.getcwd()
	print ("%s%s" %(a,"\\1"))
	b = os.listdir()
	print (b)
	c = os.path.exists("%s%s%d" %(a,"\\",i))
	print (c)
	
	if c == False:
		os.mkdir("%d" %(i))
		shutil.copyfile("1.dat","%s%s%d\\2.dat" %(a,"\\",i)) 
		os.rename("%s%s%d\\2.dat" %(a,"\\",i),"%s%s%d%s%d.dat" %(a,"\\",i,"\\",i))
		
	#shutil.rmtree("%s%s%d" %(a,"\\",i))

	
a = os.getcwd()
print ("%s%s" %(a,"\\1"))