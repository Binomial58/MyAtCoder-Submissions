Q=int(input())
C=[0]*(10**6)
ans=[]
a=0
for i in range(Q):
    t,*x=map(int, input().split())
    if t==1:
        if C[x[0]-1]==0:
            a+=1
        C[x[0]-1]+=1
    elif t==2:
        if C[x[0]-1]==1:
            a-=1
        C[x[0]-1]-=1
    else:
        ans.append(a)
for l in ans:
    print(l)