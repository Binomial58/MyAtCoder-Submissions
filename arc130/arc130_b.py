h, w, c, q = map(int, input().split())
T = []
C = [0 for i in range(c)]
H = dict()
W = dict()
for i in range(q):
    t, n, c = map(int, input().split())
    if t == 1:
        H[n] = w
    else:
        W[n] = h
    T.append([t, n, c])
# print(C)
# print(H)
# print(W)
hc = 0
wc = 0
for i in range(q - 1, -1, -1):
    t, n, c = T[i]
    if t == 1:
        C[c - 1] += max(H[n] - hc, 0)
        if H[n] != 0:
            wc += 1
        H[n] = 0
    else:
        C[c - 1] += max(W[n] - wc, 0)
        if W[n] != 0:
            hc += 1
        W[n] = 0
    # print(t, n, c)
print(*C)
