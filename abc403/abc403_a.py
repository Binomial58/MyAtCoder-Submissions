N=int(input())
A=list(map(int, input().split()))
S=0
for i in range(N):
    if (i+1)%2==1:
        S+=A[i]
print(S)