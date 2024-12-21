H,W,X,Y=map(int, input().split())
S=[]
T=int(0)
for k in range(H):
    S.append(list(input()))
T=input()
for i in range(len(T)):
    if T[i]=="U" and S[X-2][Y-1]!="#":
        X-=1
        if S[X-1][Y-1]=="@":
            S[X-1][Y-1]="|"
    if T[i]=="D" and S[X][Y-1]!="#":
        X+=1
        if S[X-1][Y-1]=="@":
            S[X-1][Y-1]="|"
    if T[i]=="R" and S[X-1][Y]!="#":
        Y+=1
        if S[X-1][Y-1]=="@":
            S[X-1][Y-1]="|"
    if T[i]=="L" and S[X-1][Y-2]!="#":
        Y-=1
        if S[X-1][Y-1]=="@":
            S[X-1][Y-1]="|"
T=sum(row.count("|")for row in S)
print(X,Y,T)