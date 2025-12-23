import itertools

n, m = map(int, input().split())
V = [[False for i in range(n)] for i in range(n)]
W = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    u, v, w = map(int, input().split())
    V[u - 1][v - 1] = True
    V[v - 1][u - 1] = True
    W[u - 1][v - 1] = w
    W[v - 1][u - 1] = w
Q = [i for i in range(1, n)]
now = 2**70
for q in itertools.permutations(Q):
    P = [0]
    for i in q:
        P.append(i)
        if i == n - 1:
            break
    x = 0
    flag = True
    for k in range(len(P) - 1):
        if V[P[k]][P[k + 1]]:
            x ^= W[P[k]][P[k + 1]]
        else:
            flag = False
            break
    if flag:
        now = min(x, now)
    # print(P)
    # print(now)
# print(V)
# print(W)
print(now)
