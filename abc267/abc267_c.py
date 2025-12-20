n, m = map(int, input().split())
A = list(map(int, input().split()))
As = [A[i] for i in range(n)]
for i in range(1, n):
    As[i] += As[i - 1]
As = [0] + As
now = 0
for i in range(m):
    now += A[i] * (i + 1)
# print(now)
# print(As)
r = now
for i in range(n - m):
    now -= As[i + m] - As[i]
    now += A[i + m] * m
    r = max(r, now)
print(r)
