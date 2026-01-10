n, q = map(int, input().split())
now = 0
R = []
H = [1 for i in range(n)]
P = dict()
for i in range(n):
    P[i] = i
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p = query[1] - 1
        h = query[2] - 1
        H[P[p]] -= 1
        if H[P[p]] == 1:
            now -= 1
        P[p] = h
        H[P[p]] += 1
        if H[P[p]] == 2:
            now += 1
    else:
        R.append(now)
# print(H)
# print(P)
for r in R:
    print(r)
