n, q = map(int, input().split())
R = []
P = [i + 1 for i in range(n)]
now = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, x = query[1], query[2]
        P[(p + now - 1) % n] = x
    elif query[0] == 2:
        p = query[1]
        R.append(P[(p + now - 1) % n])
    else:
        k = query[1]
        now += k
for r in R:
    print(r)
