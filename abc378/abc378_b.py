N=int(input())
q=[]
r=[]
for i in range(N):
    L,M=map(int,input().split())
    q.append(L)
    r.append(M)
Q=int(input())
t=[]
d=[]
for k in range(Q):
    L,M=map(int,input().split())
    t.append(L)
    d.append(M)
for j in range(Q):
    #ごみの種類の配列への対応
    X=t[j]-1
    if d[j]<=r[X]:
        print(r[X])
    else:
        Z=d[j]%q[X]
        if Z==r[X]:
            print(d[j])
        elif Z>r[X]:
            Y=q[X]+r[X]-Z
            d[j]+=Y
            print(d[j])
        else:
            Y=r[X]-Z
            d[j]+=Y
            print(d[j])