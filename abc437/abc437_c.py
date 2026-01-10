t = int(input())
R = []
for i in range(t):
    n = int(input())
    P = []
    ws = 0
    ps = 0
    for j in range(n):
        w, p = map(int, input().split())
        P.append([w, p, w + p])
        ws += w
    P = sorted(P, reverse=True, key=lambda x: x[2])
    # print(P)
    count = 0
    while ws > ps:
        ws -= P[count][0]
        ps += P[count][1]
        count += 1
    R.append(n - count)
for r in R:
    print(r)
