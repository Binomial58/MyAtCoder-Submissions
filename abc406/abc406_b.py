n, k = map(int, input().split())
A = list(map(int, input().split()))
now = 1
for i in range(n):
    now *= A[i]
    if len(str(now)) >= k + 1:
        now = 1
print(now)
