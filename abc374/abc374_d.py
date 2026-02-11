import itertools
import math

n, s, t = map(int, input().split())
time = 10**20
G = []
A = [2 * i for i in range(n)]
# print(A)
for i in range(n):
    a, b, c, d = map(int, input().split())
    G.append([a, b])
    G.append([c, d])
# print(G)
for a in itertools.permutations(A):
    # print(a)
    for i in range(1 << n):
        B = [0 for k in range(n)]
        for j in range(n):
            if (i >> j) & 1:
                B[j] = 1
        C = []
        for k in range(n):
            if B[k] == 0:
                C.append(a[k])
                C.append(a[k] + 1)
            else:
                C.append(a[k] + 1)
                C.append(a[k])
        # print(C)
        now = 0
        x, y = 0, 0
        for k in range(n):
            # print(C[2 * k], C[2 * k + 1])
            now += math.sqrt((x - G[C[2 * k]][0]) ** 2 + (y - G[C[2 * k]][1]) ** 2) / s
            x = G[C[2 * k]][0]
            y = G[C[2 * k]][1]
            now += (
                math.sqrt((x - G[C[2 * k + 1]][0]) ** 2 + (y - G[C[2 * k + 1]][1]) ** 2)
                / t
            )
            x = G[C[2 * k + 1]][0]
            y = G[C[2 * k + 1]][1]
        time = min(time, now)
        # print(B)
# print(G)
print(time)
