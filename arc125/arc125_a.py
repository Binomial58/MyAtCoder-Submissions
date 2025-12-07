n, m = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
R = []
if len(set(S)) < len(set(T)) or set(S).isdisjoint(set(T)):
    print(-1)
    exit()
# まず0と1が隣接している場所を見つける．
A = S + S
i = 0
# print(A)
# print(A[n - i], A[n + i], S[0])
if T[0] == S[0]:
    if len(S) != 1 and len(set(T)) != 1:
        while A[n - i] == S[0] and A[n + i] == S[0]:
            # print(A[n - i], A[n + i], S[0])
            i += 1
        i -= 1
else:
    if len(S) != 1:
        while A[n - i] == S[0] and A[n + i] == S[0]:
            # print(A[n - i], A[n + i], S[0])
            i += 1
        i -= 1
# このiでoと1の境目にいる．
Count = 0
Count += i + m
if S[0] != T[0]:
    Count += 1
for k in range(1, len(T)):
    if T[k - 1] != T[k]:
        Count += 1
print(Count)
