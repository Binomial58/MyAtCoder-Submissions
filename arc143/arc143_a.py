X=list(map(int, input().split()))
X.sort()
K=X[2]
if 2*K-X[0]-X[1]<=K:
    print(K)
else:
    print(-1)