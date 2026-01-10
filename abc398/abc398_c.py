from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
ans = -1
maxn = 0
for i in range(n):
    a = A[i]
    if C[a] == 1:
        maxn = max(maxn, A[i])
        if maxn == A[i]:
            ans = i + 1
print(ans)
