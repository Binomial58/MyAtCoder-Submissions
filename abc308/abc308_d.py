from collections import deque

h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
Sn = ["s", "n", "u", "k", "e"]
vec = [[0, 1], [0, -1], [1, 0], [-1, 0]]
Q = deque()
Visited = [[False for i in range(w)] for j in range(h)]
if S[0][0] != "s":
    print("No")
else:
    # 行数，列数，移動回数
    Q.append([0, 0, 0])
    Visited[0][0] = True
    while len(Q):
        y, x, count = Q.pop()
        for vy, vx in vec:
            dy = y + vy
            dx = x + vx
            if (
                0 <= dy <= h - 1
                and 0 <= dx <= w - 1
                and not Visited[dy][dx]
                and S[dy][dx] == Sn[(count + 1) % 5]
            ):
                Q.append([dy, dx, count + 1])
                Visited[dy][dx] = True
    if Visited[h - 1][w - 1]:
        print("Yes")
    else:
        print("No")
