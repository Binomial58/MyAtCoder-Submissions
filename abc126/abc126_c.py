import math

n, k = map(int, input().split())
count = 0
for i in range(1, n + 1):
    if i >= k:
        count += 1 / n
    else:
        c = math.ceil(math.log2(k / i))
        count += 1 / (n * 2**c)
print(count)
