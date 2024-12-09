N=int(input())
T=0
V=0
M=[0]
for i in range(N):
    t,v=map(int,input().split())
    M.append(t)
    T=t-M[i]
    if V!=0:
        V=V-T
        if V<0:
            V=0
        V+=v
    else:
        V+=v
print(V)