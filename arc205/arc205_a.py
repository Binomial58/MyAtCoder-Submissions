n, q = map(int, input().split())
S = [list(input()) for _ in range(n)]
sumS = [[0 for i in range(n)] for i in range(n)]
for i in range(n - 1):
    for j in range(n - 1):
        if S[i][j] == S[i + 1][j] == S[i][j + 1] == S[i + 1][j + 1] == ".":
            sumS[i + 1][j + 1] += 1
for i in range(n):
    for j in range(1, n):
        sumS[i][j] += sumS[i][j - 1]
for j in range(n):
    for i in range(1, n):
        sumS[i][j] += sumS[i - 1][j]
R = []
for i in range(q):
    u, d, l, r = map(int, input().split())
    R.append(
        sumS[d - 1][r - 1]
        - sumS[u - 1][r - 1]
        - sumS[d - 1][l - 1]
        + sumS[u - 1][l - 1]
    )
for r in R:
    print(r)
