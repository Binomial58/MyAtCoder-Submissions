X=list(map(int, input().split()))
X.sort()
K=int(input())
for i in range(K):
    X[-1]*=2
print(sum(X))