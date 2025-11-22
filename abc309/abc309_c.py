import bisect

n, k = map(int, input().split())
A = []
# 日付の種類
SA = set()
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    SA.add(a)
    B.append(b)
SA = list(SA)
SA.sort()
# 日付と錠剤の対応
D = {}
for s in SA:
    D[s] = 0
for i in range(n):
    D[A[i]] += B[i]
# 累積個数
S = []
for s in SA:
    S.append(D[s])
for i in range(1, len(S)):
    S[i] += S[i - 1]
if k >= S[-1]:
    print(1)
else:
    d = bisect.bisect_left(S, S[-1] - k)
    print(SA[d] + 1)
