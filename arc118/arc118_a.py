import math

t, n = map(int, input().split())
# d = (100 + t) / 100 - 1
# print(d)
# P = []
# for i in range(1, n + 1):
#     if 100 * i % t == 0:
#         P.append(100 * i // t - 1)
#     else:
#         P.append(100 * i // t)
# for p in P:
#     print((100 + t) / 100 * p)
if 100 * n % t == 0:
    p = 100 * n // t - 1
else:
    p = 100 * n // t
print(math.ceil((100 + t) / 100 * p))
