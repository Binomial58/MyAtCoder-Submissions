a, k = map(int, input().split())
if k == 0:
    print(2 * 10**12 - a)
else:
    day = 0
    while a < 2 * 10**12:
        a += 1 + k * a
        day += 1
    print(day)