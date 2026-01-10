n = int(input())
S = [list(input()) for _ in range(n)]
flag = False
for i in range(n):
    for j in range(n - 6 + 1):
        count = 0
        for k in range(6):
            if S[i][j + k] == "#":
                count += 1
        if count >= 4:
            flag = True

for j in range(n):
    for i in range(n - 6 + 1):
        count = 0
        for k in range(6):
            if S[i + k][j] == "#":
                count += 1
        if count >= 4:
            flag = True

for i in range(n - 6 + 1):
    for j in range(n - 6 + 1):
        count = 0
        for k in range(6):
            if S[i + k][j + k] == "#":
                count += 1
        if count >= 4:
            flag = True

for i in range(n - 1, 4, -1):
    for j in range(n - 6 + 1):
        count = 0
        for k in range(6):
            if S[i - k][j + k] == "#":
                count += 1
        if count >= 4:
            flag = True
    # print(i)

if flag:
    print("Yes")
else:
    print("No")
