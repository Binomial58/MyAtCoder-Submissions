n = int(input())
now = 1
for i in range(1, n + 1):
    now *= i
    now %= 10**9 + 7
print(now)
