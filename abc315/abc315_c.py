n = int(input())
F = []
S = []
for i in range(n):
    f, s = map(int, input().split())
    F.append(f)
    S.append(s)
S, F = zip(*sorted(zip(S, F), reverse=True))
maxs = 0
for i in range(1, n):
    if F[i] == F[0]:
        maxs = max(maxs, S[0] + S[i] // 2)
    else:
        maxs = max(maxs, S[0] + S[i])
print(maxs)
