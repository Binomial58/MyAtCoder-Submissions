N=int(input())
V=list(map(int, input().split()))
C=list(map(int, input().split()))
S=0
for i in range(N):
    if V[i]-C[i]>=0:
        S+=V[i]-C[i]
print(S)