from collections import deque

n, m = map(int, input().split())
V = [set() for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    V[a - 1].add(b - 1)
# print(V)
count = 0
for i in range(n):
    Visited = [False for i in range(n)]
    Q = deque()
    Q.append(i)
    Visited[i] = True
    count += 1
    while Q:
        q = Q.pop()
        for v in V[q]:
            if not Visited[v]:
                Q.append(v)
                Visited[v] = True
                count += 1
print(count)
