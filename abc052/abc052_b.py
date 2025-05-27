N=int(input())
S=input()
m=0
x=0
for s in S:
    if s=="I":
        x+=1
    else:
        x-=1
    m=max(m,x)
print(m)