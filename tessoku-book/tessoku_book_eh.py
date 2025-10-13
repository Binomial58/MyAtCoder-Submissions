n,m=map(int, input().split())
X=[0 for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    X[a-1]+=1
    X[b-1]+=1
print(X.index(max(X))+1)