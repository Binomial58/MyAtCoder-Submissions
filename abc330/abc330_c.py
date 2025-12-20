import math

d = int(input())
k = math.sqrt(d / 2)
m = 10**10
for x in range(math.ceil(k) + 1):
    c = d - x**2
    if c < 0:
        m = min(m, -c)
    else:
        m = min(
            m,
            abs(c - math.floor(math.sqrt(c)) ** 2),
            abs(c - math.ceil(math.sqrt(c)) ** 2),
        )
print(m)
