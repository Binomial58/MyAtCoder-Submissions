import math
import itertools


def distance(x_1, y_1, x_2, y_2):
    return math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


n = int(input())
X = []
Y = []
p = 1
for i in range(n, 0, -1):
    p *= i
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
C = [i for i in range(n)]
now = 0
for c in itertools.permutations(C):
    for i in range(n - 1):
        now += distance(X[c[i]], Y[c[i]], X[c[i + 1]], Y[c[i + 1]])
print(now / p)
