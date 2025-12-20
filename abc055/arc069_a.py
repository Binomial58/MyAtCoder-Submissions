n, m = map(int, input().split())
count = 0
count += min(n, m // 2)
n -= count
m -= 2 * count
count += m // 4
# print(n, m)
print(count)
