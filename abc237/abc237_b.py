H,W=map(int, input().split())
A=[]
for _ in range(H):
    a=list(map(int, input().split()))
    A.append(a)
B=[]
for i in range(W):
    b=[]
    for j in range(H):
        b.append(A[j][i])
    B.append(b)
for c in range(W):
    print(*B[c])