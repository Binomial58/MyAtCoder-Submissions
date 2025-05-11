N=int(input())
L=[i for i in range(1,N+1)]
P=list(map(int, input().split()))
C=0
for i in range(N):
    if L[i]!=P[i]:
        C+=1
if C==2 or C==0:
    print("YES")
else:
    print("NO")