import math
n=int(input())
R=[]
for i in range(n):
    r=int(input())  
    R.append(r)
R.sort(reverse= True)
S=0
for i in range(n):
    if i %2==0:
        S+=math.pi*R[i]**2
    else:
        S-=math.pi*R[i]**2
print(S)