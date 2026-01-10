from collections import deque

n, m = map(int, input().split())
V = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    V[y - 1].append(x - 1)
# print(V)
R = []
q = int(input())
Visited = [False] * n
for i in range(q):
    x, v = list(map(int, input().split()))
    v -= 1
    if x == 1:
        Q = deque()
        Q.append(v)
        if Visited[v]:
            continue
        Visited[v] = True
        while len(Q) != 0:
            w = Q.popleft()
            for dw in V[w]:
                if not Visited[dw]:
                    Visited[dw] = True
                    Q.append(dw)
    else:
        if Visited[v]:
            R.append("Yes")
        else:
            R.append("No")
    # print(Visited)
for r in R:
    print(r)
