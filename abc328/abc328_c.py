n,q=map(int, input().split())
s=input()
R=[]
P=[]
U=[0]
for i in range(n-1):
    if s[i]==s[i+1]:
        P.append(1)
    else:
        P.append(0)
for i in range(n-1):
    U.append(U[-1]+P[i])
for i in range(q):
    l,r=map(int, input().split())
    l-=1
    r-=1
    R.append(U[r]-U[l])
for r in R:
    print(r)