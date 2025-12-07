import bisect

n = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
for i in range(1, n):
    P[i] += P[i - 1]
P = [0] + P
q = int(input())
R = []
for i in range(q):
    l, r = map(int, input().split())
    li = bisect.bisect_left(X, l)
    ri = bisect.bisect(X, r)
    R.append(P[ri] - P[li])
for r in R:
    print(r)
