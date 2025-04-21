N=int(input())
S=100000000000
for i in range(1,N):
    A=str(i)
    B=str(N-i)
    X=0
    for j in range(len(A)):
        X+=int(A[j])
    for k in range(len(B)):
        X+=int(B[k])
    S=min(S,X)
print(S)
