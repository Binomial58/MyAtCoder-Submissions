n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
s = (n * (n - 1) * (n - 2)) // 6
for a in range(n):
    for b in range(n):
        for c in range(n):
            if a < b < c:
                p = (Y[a] - Y[b]) * (X[a] - X[c])
                q = (Y[a] - Y[c]) * (X[a] - X[b])
                if p == q:
                    s -= 1
print(s)
