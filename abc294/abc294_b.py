H,W=map(int, input().split())
A=[list(map(int, input().split()))for _ in range(H)]
B=[chr(i) for i in range(65,91)]
for k in range(H):
    S=""
    for j in range(W):
        if A[k][j]==0:
            S+="."
        else:
            S+=B[A[k][j]-1]
    print(S)