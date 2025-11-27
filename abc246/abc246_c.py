n, k, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
for i in range(n):
    m = min(A[i] // x, k)
    if m == 0:
        break
    else:
        if A[i] // x <= k:
            k -= A[i] // x
            A[i] %= x
        else:
            A[i] -= x * k
            k = 0
A.sort(reverse=True)
print(sum(A[k:]))
# print(A, k)
