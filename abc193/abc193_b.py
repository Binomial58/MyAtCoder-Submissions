N=int(input())
P,X=[],[]
C=10**10
for _ in range(N):
    a,p,x=map(int, input().split())
    P.append(p)
    X.append(x-a)
for i in range(N):
    if X[i]>0:
        C=min(C,P[i])
if C==10**10:
    print(-1)
else:
    print(C)