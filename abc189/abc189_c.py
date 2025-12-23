n = int(input())
A = list(map(int, input().split()))
m = 0
for l in range(n):
    x = A[l]
    for r in range(l, n):
        x = min(x, A[r])
        m = max(m, x * (r - l + 1))
        # print(l, r)
print(m)
