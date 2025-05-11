N=int(input())
W=list(map(int, input().split()))
m=10**10
for i in range(N):
    S=abs(sum(W[i:])-sum(W[:i]))
    m=min(S,m)
print(m)