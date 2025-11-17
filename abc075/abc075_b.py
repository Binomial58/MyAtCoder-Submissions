h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
S = [["." for i in range(w)]] + S + [["." for i in range(w)]]
R = [[0 for i in range(w)] for j in range(h)]
vec = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
for i in range(h + 2):
    S[i] = ["."] + S[i] + ["."]
for i in range(1, w + 1):
    for j in range(1, h + 1):
        count = 0
        if S[j][i] == ".":
            for v in vec:
                if S[j + v[0]][i + v[1]] == "#":
                    count += 1
            R[j - 1][i - 1] = str(count)
        else:
            R[j - 1][i - 1] = "#"
for r in R:
    print("".join(r))
