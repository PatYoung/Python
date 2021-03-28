import easygui as g
a = []
b = []
c = []
s = 0
l = 0
sb = 0
sd = 0
i = 0
n = 0
l = 0

#n = input("How many lessons?")
msg = "How many required courses?"
title = "Required courses"
fieldNames = ["How many"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg,title, fieldNames)
n = int(fieldValues[0])

while i < n :
    msg = "Enter grade and point(Fill the lattice and go on)"
    title = "Grade and Point"
    fieldNames = ["Grade","Grade point"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = g.multenterbox(msg,title, fieldNames)
    fieldValues[0] = int(fieldValues[0])
    fieldValues[1] = int(fieldValues[1])
    a.append(fieldValues[0])
    b.append(fieldValues[1])
    c.append(a[i]*b[i])
    i = i + 1

sb = sum(b)
s = sum(c) / sb
sd = s

i = 0

#n = input("How many extra lessons?")
msg = "How many electives?"
title = "Electives"
fieldNames = ["How many"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg,title, fieldNames)
n = int(fieldValues[0])

while i < n :
    msg = "Enter grade and point(Fill the lattice and go on)"
    title = "Grade and Point"
    fieldNames = ["Grade","Grade point"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = g.multenterbox(msg,title, fieldNames)
    fieldValues[0] = int(fieldValues[0])
    fieldValues[1] = int(fieldValues[1])
    a.append(fieldValues[0])
    b.append(fieldValues[1])
    i = i + 1

i = 0
l = s
while i < n :
    #if a[i] <= s :
    #    s = s + a[i] * b[i] * 0.002
    #else :
    p = s + a[i] * b[i] * 0.002
    l = l + a[i] * b[i] * 0.002
    q =(s * sb + a[i] * b[i]) /(sb + b[i])
    if p < q :
        s = q
    else :
        s = p
    i = i + 1

g.msgbox("Average of required courses: %.3f \nDirect add: %.3f \nMax grade: %.3f"% (sd,l,s), title = "The result", ok_button = "Now you see") 
#print "Class A:", sd
#print "Driect add:",l
#print "Max:",s
