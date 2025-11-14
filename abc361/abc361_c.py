n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
m = 10**9
for i in range(k + 1):
    l = n - k
    m = min(m, A[i + l - 1] - A[i])
print(m)
