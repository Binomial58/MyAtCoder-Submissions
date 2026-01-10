h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]
left = 10**10
right = -1
up = 10**10
down = -1
for i in range(h):
    if "#" in S[i]:
        left = min(left, S[i].index("#"))
        right = max(right, w - S[i][::-1].index("#") - 1)
        up = min(up, i)
        down = max(down, i)
for i in range(up, down + 1):
    for j in range(left, right + 1):
        if S[i][j] == ".":
            print("No")
            exit()
print("Yes")
# print(left, right)
# print(up, down)
