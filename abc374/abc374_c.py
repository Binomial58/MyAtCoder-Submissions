def bin(N):
    C = ""
    while N != 0:
        C += str(N % 2)
        N //= 2
    D = ""
    for i in range(len(C)):
        D += C[len(C) - i - 1]
    return D
N=int(input())
K=list(map(int, input().split()))
S=sum(K)
M=10**10
for i in range(2**N):
    A=S
    B=0
    k="0"*(N-len(bin(i)))+bin(i)
    for j in range(N):
        if k[j]=="1":
            B+=K[j]
    A-=B
    M=min(M,max(A,B))
print(M)
