N=int(input())
K=int(input())
X=list(map(int, input().split()))
S=0
for i in range(N):
    S+=min(2*X[i],2*abs(X[i]-K))
print(S)