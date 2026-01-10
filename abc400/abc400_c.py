import math

n = int(input())
R = set()
A = []
i = 1
count = 0
while 2**i <= n:
    A.append(2**i)
    i += 1
for a in A:
    b = math.isqrt(n // a)
    b = math.ceil(b / 2)
    count += b
    # print(a, b)
print(count)
