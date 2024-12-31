N,Q=map(int, input().split())
E=[list(map(int,input().split())) for _ in range(Q)]
P=[0]*N
for q in range(Q):
    if E[q][0]==1:
        P[E[q][1]-1]+=1
    elif E[q][0]==2:
        P[E[q][1]-1]+=2
    else:
        if P[E[q][1]-1]>1:
            print("Yes")
        else:
            print("No")