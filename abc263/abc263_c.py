from itertools import *

n, m = map(int, input().split())
iterable = [i + 1 for i in range(m)]
L = list(combinations(iterable, n))
for l in L:
    print(*l)
