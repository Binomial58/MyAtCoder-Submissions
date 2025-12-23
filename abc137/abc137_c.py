from collections import Counter

n = int(input())
S = []
for i in range(n):
    s = list(input())
    s.sort()
    S.append("".join(s))
# print(S)
T = Counter(S)
count = 0
for t in T:
    count += T[t] * (T[t] - 1) // 2
print(count)
