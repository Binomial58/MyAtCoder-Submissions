n = int(input())
S = [int(input()) for i in range(n)]
dp = [[False for i in range(100 * 100 + 1)] for j in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(100 * 100 + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
            dp[i + 1][j + S[i]] = True
for i in range(100 * 100, -1, -1):
    if i % 10 != 0 and dp[n][i]:
        print(i)
        exit()
print(0)
