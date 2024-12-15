N,Q=map(int, input().split())
T=list(map(int, input().split()))
teeth=[1]*N
for i in range(Q):
    if teeth[T[i]-1]==1:
        teeth[T[i]-1]=0
    else:
        teeth[T[i]-1]=1
print(sum(teeth))