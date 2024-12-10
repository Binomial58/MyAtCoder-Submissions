N,A=map(int, input().split())
T=list(map(int, input().split()))
R=0
W=0
for k in range(N):
    if T[k]>=R:
        R+=A+T[k]-W
        W=R
        print(R)
    else:
        R+=A
        W=R
        print(R)