n = int(input())
A = list(map(int, input().split()))
dp = [[0, [0, 0]] for i in range(n + 1)]
dp[0][0] = 1000
for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1][0] + dp[i - 1][1][1] * A[i - 1])
    if dp[i - 1][0] > dp[i - 1][1][0] + dp[i - 1][1][1] * A[i - 1]:
        dp[i][1][0] = dp[i - 1][0] % A[i - 1]
        dp[i][1][1] = dp[i - 1][0] // A[i - 1]
    else:
        dp[i][1][0] = dp[i - 1][1][0]
        dp[i][1][1] = dp[i - 1][1][1]
print(max(dp[-1][0], dp[-1][1][0] + dp[-1][1][1] * A[-1]))
