# 再帰を使ったDFSの描き方
def dfs(i, j, now):
    global count
    if now == k:
        count += 1
        return
    Visited[i][j] = True
    for dy, dx in vec:
        ny = i + dy
        nx = j + dx
        if (
            0 <= ny <= h - 1
            and 0 <= nx <= w - 1
            and S[ny][nx] == "."
            and not Visited[ny][nx]
        ):
            dfs(ny, nx, now + 1)
    Visited[i][j] = False


h, w, k = map(int, input().split())
S = [list(input()) for _ in range(h)]
count = 0
Visited = [[False] * w for i in range(h)]
vec = [[0, 1], [0, -1], [1, 0], [-1, 0]]
for a in range(h):
    for b in range(w):
        if S[a][b] == ".":
            dfs(a, b, 0)
print(count)
