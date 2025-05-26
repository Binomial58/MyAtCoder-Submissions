N=int(input())
S=input()
R=0
for s in S:
    if s=="A":
        R+=4
    elif s=="B":
        R+=3
    elif s=="C":
        R+=2
    elif s=="D":
        R+=1
print(R/N)