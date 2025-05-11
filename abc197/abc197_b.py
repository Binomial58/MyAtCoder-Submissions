H,W,X,Y=map(int, input().split())
X-=1
Y-=1
S=[input() for _ in range(H)]
T=0
for i in range(Y,W):
    if S[X][i]=="#":
        break
    T+=1
for i in range(Y,-1,-1):
    if S[X][i]=="#":
        break
    T+=1
R=""
for i in range(H):
    R+=S[i][Y]
for i in range(X,H):
    if R[i]=="#":
        break
    T+=1
for i in range(X,-1,-1):
    if R[i]=="#":
        break
    T+=1
print(T-3)