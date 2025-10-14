from collections import deque
n,m=map(int, input().split())
E=[[] for i in range(n)]
done=[-1 for i in range(n)]
done[0]=1
L=deque()
L.append(0)
for i in range(m):
    a,b=map(int, input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)
while len(L)!=0:
    a=L.popleft()
    done[a]=1
    for b in E[a]:
        if done[b]==-1:
            L.append(b)
if sum(done)==n:
    print("The graph is connected.")
else:
    print("The graph is not connected.")