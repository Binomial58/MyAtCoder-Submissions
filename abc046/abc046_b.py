n, k = map(int, input().split())
now = k
for i in range(n - 1):
    now *= k - 1
print(now)
