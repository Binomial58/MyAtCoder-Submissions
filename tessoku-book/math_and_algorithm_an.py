from collections import deque
n,m=map(int, input().split())
E=[[] for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
isdone=[False for i in range(n)]
time=[10**9 for i in range(n)]
L=deque()
L.append(0)
isdone[0]=True
time[0]=0
while len(L)!=0:
    b=L.popleft()
    for c in E[b]:
        time[c]=min(time[c],time[b]+1)
        if not isdone[c]:
            isdone[c]=True
            L.append(c)
for t in time:
    if t ==10**9:
        print(-1)
    else:
        print(t)