H,W=map(int, input().split())
a,b=map(int, input().split())
a=a-1
b=b-1
C=[]
for _ in range(H):
    S=input().split()
    C.append("".join(S))
C=[list(row) for row in C]
C[a][b]="x"
X=input()
L=len(X)
for k in range(L):
    if X[k]=="U" and a!=0 and C[a-1][b]!="#":
        C[a][b]="."
        C[a-1][b]="x"
        a=a-1
    elif X[k]=="L" and b!=0 and C[a][b-1]!="#":
        C[a][b]="."
        C[a][b-1]="x"
        b=b-1
    elif X[k]=="D" and a!=H-1 and C[a+1][b]!="#":
        C[a][b]="."
        C[a+1][b]="x"
        a=a+1
    elif X[k]=="R" and b!=W-1 and C[a][b+1]!="#":
        C[a][b]="."
        C[a][b+1]="x"
        b=b+1
print(a+1,b+1)