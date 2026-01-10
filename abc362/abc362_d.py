import heapq

n, m = map(int, input().split())
A = list(map(int, input().split()))
V = [[] for i in range(n)]
for i in range(m):
    u, v, b = map(int, input().split())
    V[u - 1].append((v - 1, A[v - 1] + b))
    V[v - 1].append((u - 1, A[u - 1] + b))
cur = [10**20 for i in range(n)]
cur[0] = A[0]
Decided = [False for i in range(n)]
Q = [(cur[0], 0)]
heapq.heapify(Q)
while len(Q) != 0:
    c, x = heapq.heappop(Q)
    if Decided[x]:
        continue
    Decided[x] = True
    for v, w in V[x]:
        # print(cur[v], cur[x] + w)
        if cur[v] > cur[x] + w:
            cur[v] = cur[x] + w
            heapq.heappush(Q, (cur[v], v))
print(*cur[1:])
