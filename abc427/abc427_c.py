n, m = map(int, input().split())
V = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    V[u - 1].append(v - 1)
    V[v - 1].append(u - 1)
ans = 10**10
for i in range(1 << n):
    count = 0
    # print(i)
    B = []
    W = []
    for j in range(n):
        if (i >> j) & 1:
            B.append(j)
        else:
            W.append(j)
    for b in B:
        for v in V[b]:
            if v in B:
                count += 1
    for w in W:
        for v in V[w]:
            if v in W:
                count += 1
    # print(B)
    # print(W)
    ans = min(ans, count)
print(ans // 2)
