def check(k, n):
    if k**2 - k - 2 * n - 2 <= 0:
        return True
    else:
        return False


n = int(input())
l = 0
r = 10**20
while abs(l - r) > 1:
    now = (l + r) // 2
    if check(now, n):
        l = now
    else:
        r = now
if check(r, n):
    d = r
else:
    d = l
print(n - d + 2)