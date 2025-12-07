n, q = map(int, input().split())
H = [[i, 0] for i in range(n, 0, -1)]
vec = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
R = []
h = 0
for i in range(q):
    query = list(map(str, input().split()))
    if query[0] == "1":
        c = query[1]
        nowx = H[-1][0]
        nowy = H[-1][1]
        nowx += vec[c][0]
        nowy += vec[c][1]
        H.append([nowx, nowy])
        h += 1
    else:
        # print(H)
        p = int(query[1])
        R.append(H[n + h - p])
for r in R:
    print(*r)
