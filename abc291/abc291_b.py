N=int(input())
X=list(map(int, input().split()))
X.sort()
S=0
for k in range(N,4*N):
    S+=X[k]
print(S/(3*N))