n, m = map(int, input().split())
A = []
B = []
for i in range(m):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
k = int(input())
C = []
D = []
for i in range(k):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)
maxBowl = 0
for i in range(1 << k):  # 2**Nまでの探索
    now = 0
    E = [0 for i in range(k)]
    for j in range(k):
        if (i >> j) & 1:
            E[j] = C[j]
        else:
            E[j] = D[j]
    F = set(E)
    for l in range(m):
        if A[l] in F and B[l] in F:
            now += 1
    maxBowl = max(maxBowl, now)
print(maxBowl)
