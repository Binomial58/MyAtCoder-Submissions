h, w, k = map(int, input().split())
C = [list(input()) for _ in range(h)]
cn = 0
for i in range(h):
    cn += C[i].count("#")
# print(cn)
# 赤く塗るべきマス数
cn -= k
# print(cn)
count = 0
for i in range(1 << h):
    for j in range(1 << w):
        H = []
        W = []
        now = 0
        for k in range(h):
            if (i >> k) & 1:
                H.append(k)
        for k in range(w):
            if (j >> k) & 1:
                W.append(k)
        for a in H:
            now += C[a].count("#")
        for b in W:
            for j in range(h):
                if C[j][b] == "#":
                    now += 1
        for a in H:
            for b in W:
                if C[a][b] == "#":
                    now -= 1
        # print(now)
        # print(i, j)
        # print(H, W)
        if now == cn:
            count += 1
print(count)
