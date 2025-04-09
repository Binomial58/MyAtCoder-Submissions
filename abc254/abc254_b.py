def bin(A):
    B=[0]*(len(A)+1)
    for i in range(len(A)):
        B[i]+=A[i]
    for i in range(len(A)):
        B[i+1]+=A[i]
    return B
N=int(input())
A=[1]
for i in range(N):
    print(*A)
    A=bin(A)