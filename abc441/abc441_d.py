from collections import deque

n, m, l, s, t = map(int, input().split())
V = [set() for i in range(n)]
for i in range(m):
    u, v, c = map(int, input().split())
    V[u - 1].add((v - 1, c))
# print(V)
Can = [False for i in range(n)]
Q = deque()
# 頂点，コスト，回数
Q.append((0, 0, 0))
while len(Q) != 0:
    q, cost, time = Q.pop()
    if time == l:
        if s <= cost <= t:
            Can[q] = True
    else:
        for v, c in V[q]:
            if cost + c <= t:
                Q.append((v, cost + c, time + 1))
R = []
for i in range(n):
    if Can[i]:
        R.append(i + 1)
print(*R)
