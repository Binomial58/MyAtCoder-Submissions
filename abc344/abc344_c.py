N=int(input())
A=list(map(int, input().split()))
M=int(input())
B=list(map(int, input().split()))
L=int(input())
C=list(map(int, input().split()))
Q=int(input())
X=list(map(int, input().split()))
W=set()
for a in range(N):
    for b in range(M):
        for c in range(L):
            W.add(A[a]+B[b]+C[c])
for i in range(Q):
    if X[i] in W:
        print("Yes")
    else:
        print("No")