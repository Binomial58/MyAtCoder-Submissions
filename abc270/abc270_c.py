from collections import deque

n, x, y = map(int, input().split())
V = [set() for i in range(n)]
Done = [False for i in range(n)]
Path = [-1 for i in range(n)]
R = []
for i in range(n - 1):
    u, v = map(int, input().split())
    V[u - 1].add(v - 1)
    V[v - 1].add(u - 1)
# print(V)
Q = deque()
Q.append(y - 1)
Done[y - 1] = True
while not Done[x - 1]:
    q = Q.pop()
    for v in V[q]:
        if not Done[v]:
            Done[v] = True
            Path[v] = q
            Q.append(v)
# print(Path)
now = x - 1
while now != y - 1:
    R.append(now + 1)
    now = Path[now]
R.append(y)
print(*R)
# 単純パスを求める方法
