from collections import deque

h, w = map(int, input().split())
S = [["." for i in range(w + 2)] for j in range(h + 2)]
for i in range(1, h + 1):
    s = input()
    for j in range(1, w + 1):
        S[i][j] = s[j - 1]
now = 0
vec = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
Done = [[0 for i in range(w + 2)] for i in range(h + 2)]
for i in range(h + 2):
    for j in range(w + 2):
        if S[i][j] == "#":
            Done[i][j] = 0
        else:
            Done[i][j] = -1
for i in range(h + 2):
    for j in range(w + 2):
        if Done[i][j] == 0:
            now += 1
            Q = deque()
            Q.append([i, j])
            Done[i][j] = now
            while len(Q) != 0:
                q = Q.pop()
                y = q[0]
                x = q[1]
                for v in vec:
                    dy = y + v[0]
                    dx = x + v[1]
                    if Done[dy][dx] == 0:
                        Q.append([dy, dx])
                        Done[dy][dx] = now
# for d in Done:
#     print(d)
print(now)
