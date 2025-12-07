n, x = map(int, input().split())
D = []
for i in range(n):
    D.append(list(map(int, input().split())))
dp = [[False for i in range(x + 1)] for j in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(x):
        a = D[i][0]
        b = D[i][1]
        if dp[i][j]:
            if j + a <= x:
                dp[i + 1][j + a] = True
            if j + b <= x:
                dp[i + 1][j + b] = True
if dp[n][x]:
    print("Yes")
else:
    print("No")
# print(dp[n][x])
