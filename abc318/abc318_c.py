n, d, p = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
if n % d != 0:
    for i in range(d - n % d):
        F.append(0)
S = [0 for i in range(len(F) // d)]
count = 0
i = 0
for f in F:
    S[i] += f
    count += 1
    if count % d == 0:
        i += 1
now = 0
for s in S:
    now += min(p, s)
print(now)
