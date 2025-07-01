N,Q=map(int, input().split())
H=[1 for i in range(N)]
V=[i for i in range(N)]
R=[]
C=0
for i in range(Q):
    q=list(map(int, input().split()))
    if q[0]==1:
        a=q[1]-1 #移動する鳩の番号
        b=q[2]-1 #移動先の巣の番号
        c=V[a] #移動する鳩がいる巣の番号
        H[b]+=1
        H[c]-=1
        V[a]=b
        if H[b]==2:
            C+=1
        if H[c]==1:
            C-=1
    else:
        R.append(C)
for c in R:
    print(c)