import math

t = int(input())
R = []
for i in range(t):
    n, a, b = map(int, input().split())
    if a > n:
        R.append("No")
    elif a >= n // 2:
        mb = (n - a) ** 2
        # print(mb)
        if b > mb:
            R.append("No")
        else:
            R.append("Yes")
    else:
        mb = a * (n - a)
        mb += (n - a) * (math.ceil((n - 2 * a) / 2))
        if b > mb:
            R.append("No")
        else:
            R.append("Yes")
        # print(mb)
for r in R:
    print(r)
