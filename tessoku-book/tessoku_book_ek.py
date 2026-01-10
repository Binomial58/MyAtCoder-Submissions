import heapq

n, m = map(int, input().split())
V = [[] for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    V[a - 1].append((b - 1, c))
    V[b - 1].append((a - 1, c))
cur = [10**20 for i in range(n)]
Decided = [False for i in range(n)]
cur[0] = 0
Q = [(cur[0], 0)]
heapq.heapify(Q)
while len(Q) != 0:
    c, x = heapq.heappop(Q)
    if Decided[x]:
        continue
    Decided[x] = True
    for v, w in V[x]:
        if cur[v] > c + w:
            cur[v] = c + w
            heapq.heappush(Q, (cur[v], v))
R = [n]
while R[-1] != 1:
    r = R[-1] - 1
    for v, c in V[r]:
        if cur[v] + c == cur[r]:
            R.append(v + 1)
            break
print(*R[::-1])
