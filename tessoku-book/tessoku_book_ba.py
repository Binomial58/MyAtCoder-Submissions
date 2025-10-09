import heapq
q=int(input())
L=[]
R=[]
for i in range(q):
    Q=list(map(int, input().split()))
    if Q[0]==1:
        heapq.heappush(L,Q[1])
    elif Q[0]==2:
        a=heapq.heappop(L)
        R.append(a)
        heapq.heappush(L,a)
    else:
        heapq.heappop(L)
for r in R:
    print(r)