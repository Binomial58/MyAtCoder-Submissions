N,M=map(int, input().split())
L=set([i for i in range(1,N+1)])
L=list(L-{M})
print(L[0])