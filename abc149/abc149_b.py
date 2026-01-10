a, b, k = map(int, input().split())
d = a
a = max(0, a - k)
if a == 0:
    k -= d
else:
    k = 0
print(a, max(b - k, 0))
