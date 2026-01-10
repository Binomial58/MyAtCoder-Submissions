n = int(input())
mod = 10**9 + 7
ans = 0
a = 1
b = 1
c = 1
for i in range(n):
    a *= 10
    b *= 9
    c *= 8
    a %= mod
    b %= mod
    c %= mod
print((a - 2 * b + c) % mod)
