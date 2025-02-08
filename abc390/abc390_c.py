H,W=map(int, input().split())
S=[]
L=W
R=0
U=H
D=0
B=[]
for _ in range(H):
    s=input()
    S.append(s)
for i in range(H):
    if S[i].count("#")!=0:
        l=S[i].find("#")
        L=min(L,l)
        r=S[i].rfind("#")
        R=max(R,r)
for j in range(W):
    b=""
    for k in range(H):
        b+=S[k][j]
    B.append(b)
for i in range(W):
    if B[i].count("#")!=0:
        u=B[i].find("#")
        U=min(u,U)
        d=B[i].rfind("#")
        D=max(d,D)
for a in range(L,R+1):
    for b in range(U,D+1):
        if S[b][a]==".":
            print("No")
            exit()
print("Yes")