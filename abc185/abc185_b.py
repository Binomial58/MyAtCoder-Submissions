N,M,T=map(int, input().split())
X=N
t=0
C=0
for i in range(M):
    a,b=map(int, input().split())
    X-=a-t
    if X<=0:
        C=1
    X+=b-a
    X=min(X,N)
    t=b
X-=T-t
if X<=0:
    C=1
if C==0:
    print("Yes")
else:
    print("No")