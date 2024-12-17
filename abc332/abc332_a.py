N,S,K=map(int, input().split())
R=0
for _ in range(N):
    P,Q=map(int, input().split())
    R+=P*Q
if R>=S:
    print(R)
else:
    print(R+K)