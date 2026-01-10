from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
count = 0
for c in C:
    if C[c] != 1:
        count += (n - C[c]) * (C[c]) * (C[c] - 1) // 2
print(count)
