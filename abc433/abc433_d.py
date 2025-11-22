import collections

n, m = map(int, input().split())
A = list(map(int, input().split()))
L = []
for i in range(n):
    L.append(len(str(A[i])) - 1)
    A[i] %= m
Rank = [10**i % m for i in range(1, max(L) + 2)]
Ranka = [[] for i in range(len(Rank))]
for i in range(len(Rank)):
    r = Rank[i]
    for a in A:
        Ranka[i].append(a * r % m)
# print(L)
# print(A)
# print(Rank)
# print(Ranka)
count = 0
R = []
for r in Ranka:
    R.append(collections.Counter(r))
# print(R)
for i in range(n):
    # x*10**kで満たしてほしい値
    d = (m - A[i]) % m
    # print(R[L[i]][d])
    count += R[L[i]][d]
print(count)
