from collections import deque

h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
D = [[10**9 for i in range(w)] for j in range(h)]
R = [["#" for i in range(w)] for i in range(h)]
Q = deque()
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            D[i][j] = -1
        elif S[i][j] == "E":
            Q.append([i, j])
            D[i][j] = 0
vec = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while len(Q) != 0:
    # BFSはpopleft
    q = Q.popleft()
    qx = q[1]
    qy = q[0]
    for v in vec:
        dx = qx + v[1]
        dy = qy + v[0]
        if 0 <= dx <= w - 1 and 0 <= dy <= h - 1 and D[dy][dx] != -1:
            if D[qy][qx] + 1 < D[dy][dx]:
                D[dy][dx] = D[qy][qx] + 1
                Q.append([dy, dx])
for i in range(h):
    for j in range(w):
        if D[i][j] == 0:
            R[i][j] = "E"
        else:
            nx = j
            ny = i
            d = D[i][j]
            for v in vec:
                dx = nx + v[1]
                dy = ny + v[0]
                if (
                    0 <= dx <= w - 1
                    and 0 <= dy <= h - 1
                    and d > D[dy][dx]
                    and D[dy][dx] != -1
                ):
                    if v == (0, 1):
                        R[i][j] = ">"
                    elif v == (0, -1):
                        R[i][j] = "<"
                    elif v == (1, 0):
                        R[i][j] = "v"
                    else:
                        R[i][j] = "^"
# for d in D:
#     print(d)
for r in R:
    print("".join(r))
