import math

n = int(input())
for i in range(1, n + 1):
    count = 0
    for x in range(1, 101):
        for y in range(1, 101):
            a = 1
            b = x + y
            c = x**2 + y**2 + x * y - i
            if b**2 - 4 * a * c >= 0:
                z1 = (-b + math.sqrt(b**2 - 4 * a * c)) / 2
                z2 = (-b - math.sqrt(b**2 - 4 * a * c)) / 2
                if z1 > 0:
                    p = math.floor(z1)
                    q = p + 1
                    if (
                        x**2 + y**2 + p**2 + x * y + p * x + p * y == i
                        or x**2 + y**2 + q**2 + x * y + q * x + q * y == i
                    ):
                        count += 1
                if z2 > 0:
                    p = math.floor(z2)
                    q = p + 1
                    if (
                        x**2 + y**2 + p**2 + x * y + p * x + p * y == i
                        or x**2 + y**2 + q**2 + x * y + q * x + q * y == i
                    ):
                        count += 1
    print(count)
