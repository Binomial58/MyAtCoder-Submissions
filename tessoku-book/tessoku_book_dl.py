import heapq
r=0
L=[]
n,d=map(int, input().split())
X=[[] for i in range(d)]
for i in range(n):
    x,y=map(int, input().split())
    X[x-1].append(-y)
for j in range(d):
    for k in X[j]:
        heapq.heappush(L,k)
    if len(L)>0:
        r-=heapq.heappop(L)
print(r)
