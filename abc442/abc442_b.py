q=int(input())
R=[]
b=0
s=False
for i in range(q):
    a=int(input())
    if a==1:
        b+=1
    elif a==2:
        b=max(b-1,0)
    else:
        s=not s
    if s and b>=3:
        R.append("Yes")
    else:
        R.append("No")
for r in R:
    print(r)