N=int(input())
S=input()
maxS=0
s=0
d=0
#左側からの探索
for a in range(N):
    if S[a]=="-" and d==0 and a!=N-1 and S[a+1]=="o":
        d=1
        s=0
    elif S[a]=="-" and d==1 and a!=N-1 and S[a+1]!="o":
        d=0
        maxS=max(maxS,s)
        s=0
    elif d==1 and S[a]=="o":
        s+=1
    elif d==1:
        maxS=max(maxS,s)
        s=0
maxS=max(maxS,s)
#右側からの探索
s=0
d=0
for a in range(N-1,-1,-1):
    if S[a]=="-" and d==0 and a!=0 and S[a-1]=="o":
        d=1
        s=0
    elif S[a]=="-" and d==1 and a!=0 and S[a-1]!="o":
        d=0
        maxS=max(maxS,s)
        s=0
    elif d==1 and S[a]=="o":
        s+=1
    elif d==1:
        maxS=max(maxS,s)
        s=0
maxS=max(maxS,s)
if maxS>0:
    print(maxS)
else:
    print(-1)