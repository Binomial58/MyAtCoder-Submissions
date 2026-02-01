n, k = map(int, input().split())
now = 0
i = 0
while now < k:
    now += n
    n += 1
    i += 1
print(i - 1)
