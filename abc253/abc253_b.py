def manhattan(x,y,a,b) :
    return abs(x-a)+abs(y-b)
H,W=map(int, input().split())
S=[]
A=[-1,-1]
B=[-1,-1]
for i in range(H):
    w=input()
    S.append(w)
for a in range(H):
    for b in range(W):
        if S[a][b]=="o":
            if A[0]==-1:
                A=[a,b]
            else:
                B=[a,b]
print(manhattan(A[0],A[1],B[0],B[1]))
        