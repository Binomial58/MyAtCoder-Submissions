N=int(input())
A=list(map(int, input().split()))
M=0
S=0
for i in range(N):
    if M>A[i]:
        S+=M-A[i]
    else:
        M=A[i]
print(S)