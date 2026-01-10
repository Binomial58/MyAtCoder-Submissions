import heapq

q = int(input())
R = []
S = []
heapq.heapify(S)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(S, query[1])
    else:
        R.append(heapq.heappop(S))
for r in R:
    print(r)
