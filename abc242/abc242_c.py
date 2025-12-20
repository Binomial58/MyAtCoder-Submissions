n = int(input())
dp = [[0 for i in range(9)] for i in range(n)]
for i in range(9):
    dp[0][i] = 1
# print(dp)
for i in range(1, n):
    for j in range(9):
        if j == 0:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j + 1]) % 998244353
        elif j == 8:
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 998244353
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % 998244353
# print(dp)
print(sum(dp[n - 1]) % 998244353)
