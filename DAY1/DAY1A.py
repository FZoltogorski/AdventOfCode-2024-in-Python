file =  open("data.txt","r")
L = []
R = []
for line in file:
    L.append(line.split()[0])
    R.append(line.split()[1])
    
L.sort()
R.sort()

outcome = 0

for i in range(len(L)):
    outcome += abs(int(L[i])-int(R[i]))

print(outcome)
    
