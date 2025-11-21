h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
# count = 0
for i in range(h):
    for j in range(w - 4):
        # count += 1
        t = "".join([S[i][j + t] for t in range(5)])
        if t == "snuke":
            for k in range(5):
                print(i + 1, j + 1 + k)
            exit()
        elif t[::-1] == "snuke":
            for k in range(4, -1, -1):
                print(i + 1, j + 1 + k)
            exit()
# print(count)
# count = 0
for j in range(w):
    for i in range(h - 4):
        # count += 1
        t = "".join([S[i + t][j] for t in range(5)])
        if t == "snuke":
            for k in range(5):
                print(i + 1 + k, j + 1)
            exit()
        elif t[::-1] == "snuke":
            for k in range(4, -1, -1):
                print(i + 1 + k, j + 1)
            exit()
# print(count)
# count = 0
for i in range(h - 4):
    for j in range(w - 4):
        # count += 1
        t = "".join([S[i + e][j + e] for e in range(5)])
        if t == "snuke":
            for k in range(5):
                print(i + 1 + k, j + 1 + k)
            exit()
        if t[::-1] == "snuke":
            for k in range(4, -1, -1):
                print(i + 1 + k, j + 1 + k)
            exit()
# print(count)
# count = 0
for i in range(h - 4):
    for j in range(w - 1, 3, -1):
        # count += 1
        t = "".join([S[i + e][j - e] for e in range(5)])
        if t == "snuke":
            for k in range(5):
                print(i + 1 + k, j + 1 - k)
            exit()
        if t[::-1] == "snuke":
            for k in range(4, -1, -1):
                print(i + 1 + k, j + 1 - k)
            exit()
# print(count)
# count = 0
