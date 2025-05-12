H,W=map(int, input().split())
S=[list(input()) for _ in range(H)]
C=0
for i in range(H):
    for j in range(W-1):
        if S[i][j]=="." and S[i][j+1]==".":
            C+=1
for i in range(H-1):
    for j in range(W):
        if S[i][j]=="." and S[i+1][j]==".":
            C+=1
print(C)