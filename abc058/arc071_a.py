from collections import Counter

n = int(input())
S = []
R = []
for i in range(n):
    S.append(Counter(list(input())))
D = set(S[0])
for i in range(1, n):
    D &= set(S[i])
# print(D)
for d in D:
    m = 10**10
    for i in range(n):
        m = min(m, S[i][d])
    for j in range(m):
        R.append(d)
R.sort()
print("".join(R))
