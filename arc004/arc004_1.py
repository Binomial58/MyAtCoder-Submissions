import math

n = int(input())
X = []
Y = []
d = 0
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
for a in range(n):
    for b in range(n):
        if a != b:
            d = max(d, math.sqrt((X[a] - X[b]) ** 2 + (Y[a] - Y[b]) ** 2))
print(d)
