import random
import math

total_number = 0
select_number = 0
jugde = 0
kinds = []
selected = []
pick = []
rep = 100000
rep_record = []

number = input("number of all kinds:")
total_number = int(number)
number = input("number of all kinds:")
select_number = int(number)
print(total_number, select_number)

kinds = list(range(1,total_number+1))
print(kinds)

while len(selected) < select_number:
    x = random.randrange(1,total_number+1)
    if x in selected:
        selected = selected[:]
    else:
        selected.append(x)

print(sorted(selected))

while jugde != select_number: 
    x = random.randrange(1,total_number+1)
    if x in pick:
        jugde = jugde
    else:
        if x in selected:
            jugde += 1
        else:
            jugde = jugde
    pick.append(x)
    
# print(pick,len(pick))

def one_pick(kinds,selected,total_number,select_number):
    pick = []
    jugde = 0
    while jugde != select_number: 
        x = random.randrange(1,total_number+1)
        if x in pick:
            jugde = jugde
        else:
            if x in selected:
                jugde += 1
            else:
                jugde = jugde
        pick.append(x)
    return len(pick)

print(one_pick(kinds,selected,total_number,select_number))

for i in range(1,rep+1):
    rep_record.append(one_pick(kinds,selected,total_number,select_number))

print(len(rep_record))
#print(sorted(rep_record))

# for i in range(select_number,16):
#     print(i,":",rep_record.count(i)/rep)

# the following only works when select_number = total_number
def probability_greater(select_number,n):
    prob = 0.0
    a = 0.0
    for i in range(1,select_number):
        a = math.factorial(select_number)/math.factorial(select_number-i)/math.factorial(i)
        a = a*(1-i/select_number)**n*(-1)**(i+1)
        prob = prob + a
    return(prob)

# for i in range(select_number,16):
#     print(i,":",rep_record.count(i)/rep,probability_greater(select_number,i-1)-probability_greater(select_number,i))

# print("+++++ +++++ +++++ +++++")

def gengeral_probability_greater(total_number,select_number,n):
    prob = 0.0
    a = 0.0
    b = 0.0
    sum_b = 0.0
    n_tot = total_number
    m = select_number
    # a = m/n_tot*(1-1/n_tot)**(n-1)
    # for i in range(1,select_number):
    #     b = math.factorial(m-1)/math.factorial(m-1-i)/math.factorial(i)
    #     b = b*(1-i/(n_tot-1))**(n-1)
    #     sum_b = sum_b + b*(-1)**(i+1)

    # prob = a*(1-sum_b)
    sum_b = 0
    for i in range(0,select_number):
        a = math.factorial(m-1)/math.factorial(m-1-i)/math.factorial(i)
        b = a*(1-(i+1)/(n_tot))**(n-1)
        sum_b = sum_b + b*(-1)**(i)

    prob = m/n_tot*sum_b
    return(prob)

for i in range(select_number,16):
    print(i,":",rep_record.count(i)/rep,gengeral_probability_greater(total_number,select_number,i))


