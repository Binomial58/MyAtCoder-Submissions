k, a, b = map(int, input().split())
now = 1
if a + 1 >= b:
    print(now + k)
else:
    now += min(k, a - now)
    # print(now)
    d = k - a + 1
    # print(d)
    now += (b - a) * (d // 2)
    if d % 2 != 0:
        now += 1
    print(now)
