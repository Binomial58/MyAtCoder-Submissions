import math

l, r = map(int, input().split())
R = []
for j in range(l, l + 10**6):
    for i in range(r, l, -1):
        if math.gcd(j, i) == 1:
            R.append(i - j)
            break
print(max(R))
