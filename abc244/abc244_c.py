N=int(input())
X=[i for i in range(1,2*N+2)]
j=0
while j!=N:
    print(max(X))
    X[X.index(max(X))]=-1
    n=int(input())
    X[X.index(n)]=-1
    j+=1
print(max(X))
N=int(input())