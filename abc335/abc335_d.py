n = int(input())
X = [[0 for i in range(n)] for i in range(n)]
X[0] = [i + 1 for i in range(n)]
y = 0
x = n - 1
now = 0
c = n - 1
o = n
# 方向ベクトルを定義，右・下・左・上の順番
vec = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for i in range(n - 1):
    for j in range(2):
        for k in range(c):
            o += 1
            y += vec[now][0]
            x += vec[now][1]
            X[y][x] = o
        now += 1
        now %= 4
    c -= 1
X[n // 2][n // 2] = "T"
for x in X:
    print(*x)
