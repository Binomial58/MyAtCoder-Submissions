import math
import bisect

n = int(input())
P = [2**i for i in range(60)]
if n in P:
    print(n * P.index(n))
else:
    i = bisect.bisect(P, n)
    i -= 1
    # print(i)
    now = P[i] * i
    now += (n - P[i]) * (2 + i)
    print(now)