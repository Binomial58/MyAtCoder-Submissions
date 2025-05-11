N=int(input())
X=list(map(int, input().split()))
m=10**10
for i in range(min(X),max(X)+1):
    S=0
    for x in X:
        S+=(i-x)**2
    m=min(m,S)
print(m) 