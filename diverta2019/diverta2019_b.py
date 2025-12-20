r, g, b, n = map(int, input().split())
count = 0
for rn in range(n + 1):
    for gn in range(n + 1):
        d = n - r * rn - g * gn
        if d % b == 0 and d >= 0:
            count += 1
print(count)
