from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
count = 0
for c in C:
    if C[c] > c:
        count += C[c] - c
    elif C[c] < c:
        count += C[c]
print(count)
