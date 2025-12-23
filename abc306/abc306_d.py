n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
dp = [[0 for i in range(n + 1)] for i in range(2)]
for i in range(n):
    if X[i] == 1:
        dp[1][i + 1] = max(dp[0][i] + Y[i], dp[1][i])
        dp[0][i + 1] = dp[0][i]
    else:
        dp[0][i + 1] = max(dp[1][i] + Y[i], dp[0][i], dp[0][i] + Y[i])
        dp[1][i + 1] = dp[1][i]
# print(dp)
print(max(max(dp[0]), max(dp[1])))
