t = int(input())
R = []
for i in range(t):
    n, w = map(int, input().split())
    C = list(map(int, input().split()))
    Cn = []
    count = 0
    for k in range(n):
        if count == 0:
            Cn.append([])
        Cn[-1].append(C[k])
        count += 1
        if count == 2 * w:
            count = 0
    if n % (2 * w) != 0:
        Cn[-1] += [0] * (2 * w - len(Cn[-1]))
    s = 0
    for j in range(len(Cn)):
        for k in range(w):
            s += Cn[j][k]
    minc = s
    for j in range(2 * w):
        for k in range(len(Cn)):
            s += Cn[k][(j + w) % (2 * w)]
            s -= Cn[k][j]
        minc = min(minc, s)
    R.append(minc)
for r in R:
    print(r)
