h, w = map(int, input().split())
C = [list(input()) for _ in range(h)]
D = [[-(10**10) for i in range(w)] for j in range(h)]
D[0][0] = 1
for i in range(h):
    for j in range(w):
        if j + 1 != w and C[i][j + 1] == ".":
            D[i][j + 1] = max(D[i][j + 1], D[i][j] + 1)
        if i + 1 != h and C[i + 1][j] == ".":
            D[i + 1][j] = max(D[i + 1][j], D[i][j] + 1)
m = 0
for d in D:
    m = max(m, max(d))
print(m)
