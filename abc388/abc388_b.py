n, d = map(int, input().split())
now = 0
R = []
T = []
for i in range(n):
    T.append(list(map(int, input().split())))
for k in range(1, d + 1):
    r = 0
    for i in range(n):
        r = max(r, T[i][0] * (T[i][1] + k))
    R.append(r)
for r in R:
    print(r)
