N=int(input())
A=list(map(int, input().split()))
R=0
for k in range(N):
    R+=A[k]
    if R<0:
        R=0
print(R)