from collections import Counter
import itertools

s = list(input())

for i in range(len(s)):
    s[i] = int(s[i])
C = Counter(s)

A = []
for c in C:
    for i in range(min(3, C[c])):
        A.append(c)
for v in itertools.permutations(A, min(3, len(s))):
    # print(v)
    b = 0
    for i in range(min(3, len(s))):
        b += v[i] * 10**i
    if b % 8 == 0:
        print("Yes")
        exit()
# print(A)
print("No")
