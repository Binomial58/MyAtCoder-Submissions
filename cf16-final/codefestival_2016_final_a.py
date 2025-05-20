H,W=map(int, input().split())
S=[list(map(str,input().split())) for i in range(H)]
B=[chr(i) for i in range(65,91)]
A=[0,0]
for w in range(W):
    for h in range(H):
        if S[h][w]=="snuke":
            A[0]=B[w]
            A[1]=h+1
print(A[0]+str(A[1]))