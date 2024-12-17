import copy
N=int(input())
S=[list(map(int, input().split())) for _ in range(N)]
cmax=0
for t in range(0,24):
    T=copy.deepcopy(S)
    count=0
    for i in range(N):
        if T[i][1]+t>=24:
            T[i][1]=T[i][1]+t-24
        else:
            T[i][1]+=t
    for k in range(N):
        if 9<=T[k][1]<18:
            count+=T[k][0]
    cmax=max(count,cmax)
print(cmax)