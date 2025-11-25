file =  open("data.txt","r")
L = []
R = []
for line in file:
    L.append(line.split()[0])
    R.append(line.split()[1])
    
def n(element, list1):
    n = 0
    for el in list1:
        if element == el:
            n += 1
    return n
    

outcome = 0

for i in range(len(L)):
    outcome += int(L[i])*n(L[i],R)

print(outcome)
    
