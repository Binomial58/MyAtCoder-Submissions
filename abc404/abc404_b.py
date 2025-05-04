N=int(input())
S=[]
T=[]
B=[]
M=[1,2,3,0]
for _ in range(N):
    s=input()
    S.append(s)
for _ in range(N):
    t=input()
    T.append(t)
for i in range(4):
    B=[]
    for c in range(N):
        b=""
        for j in range(N):
            b+=S[N-j-1][c]
        B.append(b)
    S=B
    for a in range(N):
        for b in range(N):
            if S[a][b]!=T[a][b]:
                M[i]+=1
print(min(M))