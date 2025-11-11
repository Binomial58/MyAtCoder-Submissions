n = int(input())
c = 10**13
i = 1
while i * i <= n:
    if n % i == 0:
        a = i
        b = n // i
        c = min(c, a + b - 2)
    i += 1
print(c)
