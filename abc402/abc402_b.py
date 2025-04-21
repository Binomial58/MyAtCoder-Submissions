Q=int(input())
S=[]
U=[]
for q in range(Q):
    T=list(map(int, input().split()))
    if T[0]==1:
        S.append(T[1])
    else:
        U.append(S[0])
        S=S[1:]
for u in U:
    print(u) 