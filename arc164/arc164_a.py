t = int(input())
R = []
for i in range(t):
    n, k = map(int, input().split())
    now = 0
    d = n
    while d >= 3:
        now += d % 3
        d //= 3
    now += d
    if now <= k <= n:
        if (k - now) % 2 == 0:
            R.append("Yes")
        else:
            R.append("No")
    else:
        R.append("No")
    # print(now)
for r in R:
    print(r)
