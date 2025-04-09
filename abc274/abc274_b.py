H,W=map(int, input().split())
L=[0]*W
for i in range(H):
    C=input()
    for j in range(W):
        if C[j]=="#":
            L[j]+=1
print(*L)