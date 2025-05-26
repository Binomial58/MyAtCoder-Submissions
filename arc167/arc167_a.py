N,M=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
B=A[N-M:]
C=A[:N-M]
C.sort(reverse=True)
S=0
for i in range(N-M):
    B[i]+=C[i]
for b in B:
    S+=b**2
print(S)