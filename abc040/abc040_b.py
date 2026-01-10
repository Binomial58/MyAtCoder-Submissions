n = int(input())
maxn = 10 * 10
i = 1
while i * i <= n:
    d = n - i * (n // i)
    e = abs(i - n // i)
    maxn = min(maxn, d + e)
    # print(i)
    i += 1
print(maxn)
