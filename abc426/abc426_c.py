n,q=map(int, input().split())
R=[]
Z=[1 for i in range(n)]
r=0
for i in range(q):
    x,y=map(int, input().split())
    if x<r:
        R.append(0)
    else:
        s=sum(Z[r:x])
        R.append(s)
        Z[y-1]+=s
        r=x
for r in R:
    print(r)