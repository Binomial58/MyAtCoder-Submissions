x = int(input())
now = 0
while x != 1:
    now += 1
    x //= now
    # print(x, now)
print(now)
