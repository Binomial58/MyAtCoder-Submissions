from collections import deque

h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
Warp = dict()
DoneWarp = dict()
for i in range(h):
    for j in range(w):
        if S[i][j] != "#" and S[i][j] != ".":
            if S[i][j] not in Warp:
                Warp[S[i][j]] = []
                DoneWarp[S[i][j]] = False
            Warp[S[i][j]].append([i, j])
# print(Warp)
# print(DoneWarp)
Visited = [[10**10 for i in range(w)] for j in range(h)]
vec = [(1, 0), (-1, 0), (0, 1), (0, -1)]
Visited[0][0] = 0
Q = deque()
Q.append([0, 0])
while len(Q) != 0:
    y, x = Q.popleft()
    for dy, dx in vec:
        vy = y + dy
        vx = x + dx
        if 0 <= vy <= h - 1 and 0 <= vx <= w - 1:
            if S[vy][vx] != "#":
                if Visited[vy][vx] > Visited[y][x] + 1:
                    Visited[vy][vx] = Visited[y][x] + 1
                    Q.append([vy, vx])
    if S[y][x] in Warp and not DoneWarp[S[y][x]]:
        DoneWarp[S[y][x]] = True
        for vy, vx in Warp[S[y][x]]:
            if Visited[vy][vx] > Visited[y][x] + 1:
                Visited[vy][vx] = Visited[y][x] + 1
                Q.append([vy, vx])
if Visited[h - 1][w - 1] == 10**10:
    print(-1)
else:
    print(Visited[h - 1][w - 1])
