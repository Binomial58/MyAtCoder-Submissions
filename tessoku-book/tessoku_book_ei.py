from collections import deque
n,m=map(int, input().split())
E=[[]for i in range(n)]
done=[-1 for i in range(n)]
path=[-1 for i in range(n)]
R=[]
for i in range(m):
    a,b=map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
L=deque()
L.append(0)
a=-1
while a!=n-1:
    a=L.pop()
    done[a]=1
    for b in E[a]:
        if done[b]==-1:
            path[b]=a
            L.append(b)
c=n-1
while c!=-1:
    R.append(c+1)
    c=path[c]
print(*R[::-1])