a, m, l, r = map(int, input().split())
a -= l
r -= l
l = 0
a %= m
count = 0
if a == l:
    count += 1
    l = m
else:
    l = a
if l >= r:
    print(count)
else:
    print((r - l) // m + 1 + count)
# print(a, l, r)
