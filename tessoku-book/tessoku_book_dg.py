n,x,y=map(int, input().split())
A=list(map(int, input().split()))
X=set([0,1,2])
G=[0 for i in range(x)]
for i in range(x,y):
    Y=set([G[i-x]])
    Z=X-Y
    G.append(min(Z))
for i in range(y,x+y+2):
    Y=set([G[i-x],G[i-y]])
    Z=X-Y
    G.append(min(Z))
now=0
Gd=G[2:]
for a in A:
    if a<=x:
        now^=0
    else:
        now^=Gd[(a-x)%(x+y)]
if now==0:
    print("Second")
else:
    print("First")