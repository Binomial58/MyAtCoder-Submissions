N,M=map(int, input().split())
L,R=[0 for i in range(N)],[0 for i in range(N)]
Y=[]
for i in range(M):
    l,r=map(int, input().split())
    L[l-1]+=1
    R[r-1]+=1
S=0
for i in range(N):
    S+=L[i]
    Y.append(S)
    S-=R[i]
print(min(Y))