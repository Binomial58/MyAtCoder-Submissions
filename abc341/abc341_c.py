h, w, n = map(int, input().split())
t = input()
S = [list(input()) for _ in range(h)]
count = (h - 2) * (w - 2)
vec = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
for i in range(1, h - 1):
    for j in range(1, w - 1):
        x = j
        y = i
        if S[y][x] == "#":
            count -= 1
            continue
        for r in t:
            v = vec[r]
            y += v[0]
            x += v[1]
            if S[y][x] == "#":
                count -= 1
                break
print(count)
