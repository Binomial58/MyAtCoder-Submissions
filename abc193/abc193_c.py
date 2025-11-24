import math

n = int(input())
N = set()
for a in range(2, 10**5 + 1):
    for b in range(2, math.ceil(math.log(n) / math.log(a)) + 1):
        if a**b <= n:
            N.add(a**b)
print(n - len(N))
