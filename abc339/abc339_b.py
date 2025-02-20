H,W,N=map(int, input().split())
S=[]
R=0
a=0
b=0

#時計回りの場合の設定
def Wise(r):
    if r<3:
        r+=1
    else:
        r=0
    return r

#反時計回りの時の設定
def Counter(e):
    if e!=0:
        e-=1
    else:
        e=3
    return e

for _ in range(H):
    S.append(["."]*W)

for i in range(N):
    if S[a][b]==".":
        S[a][b]="#"
        R=Wise(R)
    else:
        S[a][b]="."
        R=Counter(R)
    if R==0:
        if a==0:
            a=H-1
        else:
            a-=1
    elif R==1:
        if b==W-1:
            b=0
        else:
            b+=1
    elif R==2:
        if a==H-1:
            a=0
        else:
            a+=1
    else:
        if b==0:
            b=W-1
        else:
            b-=1

for k in range(H):
    print("".join(S[k]))