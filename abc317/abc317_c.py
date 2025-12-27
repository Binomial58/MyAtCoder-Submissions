def dfs(x, now):
    global maxl
    Visited[x] = True
    for y, cost in V[x]:
        if not Visited[y]:
            dfs(y, now + cost)
    Visited[x] = False
    maxl = max(now, maxl)
    return maxl


n, m = map(int, input().split())
V = [[] for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    V[a - 1].append([b - 1, c])
    V[b - 1].append([a - 1, c])
maxl = 0
Visited = [False for i in range(n)]
for i in range(n):
    dfs(i, 0)
print(maxl)
