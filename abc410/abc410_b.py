N,Q=map(int, input().split())
X=list(map(int, input().split()))
Z=[0 for i in range(N)]
Y=[]
for i in range(Q):
    if X[i]==0:
        I=Z.index(min(Z))
        Z[I]+=1
        Y.append(I+1)
    else:
        Z[X[i]-1]+=1
        Y.append(X[i])
print(*Y)