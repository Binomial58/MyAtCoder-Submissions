n, t = map(int, input().split())
A = [int(input()) for i in range(n)]
count = t
now = 0
for i in range(n - 1):
    if A[i + 1] - A[i] <= t:
        count += A[i + 1] - A[i]
    else:
        count += t
print(count)
