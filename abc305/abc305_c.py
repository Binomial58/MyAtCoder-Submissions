H,W=map(int, input().split())
minS=501
maxS=0
R=[]
C=0
D=0
E=0
a=False
for i in range(H):
    S=input()
    R.append(S)
    if minS>S.count("#")>0:
        minS=S.count("#")
        D=i
    if S.count("#")>maxS:
        maxS=S.count("#")
        C=i
ls=R[C].index("#")
rs=R[C].rindex("#")
for k in range(ls,rs+1):
    if R[D][k]==".":
        print(D+1,k+1)