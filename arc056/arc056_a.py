a, b, k, l = map(int, input().split())
# L個買うのに安い値段
m = min(a * l, b)
now = 0
now += m * (k // l)
k %= l
now += min(m, a * k)
print(now)
