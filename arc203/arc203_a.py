import math

t = int(input())
R = []
for i in range(t):
    n, m = map(int, input().split())
    now = math.ceil(m / 2)
    d = m - now
    R.append(now + d * (n - 1))
for r in R:
    print(r)
