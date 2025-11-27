file = open("data.txt","r")

t = []
for line in file:
    t.append(line.split())

def clone(list1):
    list2 = []
    for element in list1:
        list2.append(element)
    return list2

def if_conditions(list1):
    conditions = True
    rising = False
    if int(list1[0])-int(list1[1])<0:
        rising = True
    

    if rising == True:
        for i in range(len(list1)-1):
            dif = int(list1[i])-int(list1[i+1])
            if not(dif >= -3 and dif <= -1):
                conditions = False
    else:
        for i in range(len(list1)-1):
            dif = int(list1[i])-int(list1[i+1])
            if not(dif <= 3 and dif >= 1):
                conditions = False

    if conditions == True:
        return 1
    else:
        return 0
    
n = 0
for report in t:
    for index in range(len(report)):
        if if_conditions(report) == 1:
            n +=1
            break
        report_new = clone(report)
        report_new.pop(index)
        if if_conditions(report_new) == 1:
            n +=1
            break
print(n)

