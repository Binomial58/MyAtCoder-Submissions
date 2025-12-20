from collections import Counter

n = int(input())
A = list(map(int, input().split()))
As = set(A)
C = Counter(A)
now = 0
for a in As:
    now += C[a] * (C[a] - 1) // 2
for a in A:
    if C[a] > 1:
        d = now - (C[a] * (C[a] - 1) // 2) + ((C[a] - 1) * (C[a] - 2) // 2)
        print(d)
    else:
        print(now)
# print(now)
# print(C)