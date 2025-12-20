import itertools
import collections

n, k = map(int, input().split())
S = [input() for i in range(n)]
D = dict()
A = [chr(97 + i) for i in range(26)]
for s in S:
    D[s] = collections.Counter(s)
# print(D)
m = 0
for j in range(k, n + 1):
    for v in itertools.combinations(S, j):
        B = [0 for i in range(26)]
        for u in v:
            for i in range(26):
                B[i] += D[u][A[i]]
        m = max(m, B.count(k))
print(m)