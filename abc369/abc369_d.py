n = int(input())
A = list(map(int, input().split()))
dp = [[0 for i in range(n)] for j in range(2)]
dp[0][0] = A[0]
for i in range(1, n):
    dp[1][i] = max(dp[0][i - 1] + 2 * A[i], dp[1][i - 1])
    dp[0][i] = max(dp[1][i - 1] + A[i], dp[0][i - 1])
print(max(dp[1][-1], dp[0][-1]))
