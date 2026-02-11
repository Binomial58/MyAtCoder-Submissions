from collections import deque

h, w = map(int, input().split())
# 0はスイッチを押す前・1はスイッチを押した後
A = [[["." for i in range(w)] for j in range(h)] for k in range(2)]
for i in range(h):
    B = list(input())
    for j in range(w):
        if B[j] == "S":
            Sx, Sy = j, i
        elif B[j] == "G":
            Gx, Gy = j, i
        A[0][i][j] = B[j]
        if B[j] == "o":
            A[1][i][j] = "x"
        elif B[j] == "x":
            A[1][i][j] = "o"
        else:
            A[1][i][j] = B[j]
Turn = [[[10**9 for i in range(w)] for j in range(h)] for k in range(2)]
Turn[0][Sy][Sx] = 0
Vec = {(1, 0), (-1, 0), (0, 1), (0, -1)}
Q = deque()
# 状態・y座標・x座標
Q.append((0, Sy, Sx))
# print(Sy, Sx)
while len(Q) != 0:
    now, y, x = Q.popleft()
    turn = Turn[now][y][x]
    # print(now, y, x)
    for v in Vec:
        dy = y + v[0]
        dx = x + v[1]
        if (
            0 <= dy <= h - 1
            and 0 <= dx <= w - 1
            and A[now][dy][dx] != "#"
            and A[now][dy][dx] != "x"
        ):
            if A[now][dy][dx] == "?":
                now2 = 1 - now
            else:
                now2 = now
            # print(now2, dy, dx)
            if Turn[now2][dy][dx] > turn + 1:
                Turn[now2][dy][dx] = turn + 1
                Q.append((now2, dy, dx))
            # print(dy, dx)
# print(Turn[0])
# print(Turn[1])
d = min(Turn[0][Gy][Gx], Turn[1][Gy][Gx])
if d == 10**9:
    print(-1)
else:
    print(d)
