import bisect

n = int(input())
X = []
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
S = sorted(list(set(A)))
ranking = {x: i + 1 for i, x in enumerate(S)}
A_zaatsu = []
for a in A:
    A_zaatsu.append(ranking[a])
S = sorted(list(set(B)))
ranking = {x: i + 1 for i, x in enumerate(S)}
B_zaatsu = []
for b in B:
    B_zaatsu.append(ranking[b])
# print(A_zaatsu)
# print(B_zaatsu)
AB = []
for i in range(n):
    AB.append([A_zaatsu[i], B_zaatsu[i]])
# print(AB)
AB = sorted(AB, key=lambda x: (x[0], -x[1]))
INF = 1 << 30
dp = [INF] * (n + 1)
for a, b in AB:
    i = bisect.bisect_left(dp, b)
    dp[i] = b
ans = bisect.bisect_left(dp, INF)
print(ans)
