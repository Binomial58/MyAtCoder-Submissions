h, w = map(int, input().split())
S = [["." for i in range(w + 2)] for j in range(h + 2)]
for i in range(1, h + 1):
    s = input()
    for j in range(1, w + 1):
        S[i][j] = s[j - 1]
vec = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if S[i][j] == "#":
            c = False
            for v in vec:
                y = i + v[0]
                x = j + v[1]
                if S[y][x] == "#":
                    c = True
            if not c:
                print("No")
                exit()
print("Yes")
