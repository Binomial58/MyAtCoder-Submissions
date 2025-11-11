n = int(input())
A = [[], []]
A[0] = list(map(int, input().split()))
A[1] = list(map(int, input().split()))
dp = [[-(10**9) for i in range(n)] for i in range(2)]
dp[0][0] = A[0][0]
dp[1][0] = dp[0][0] + A[1][0]
for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + A[0][i]
for i in range(1, n):
    dp[1][i] = max(dp[1][i - 1] + A[1][i], dp[0][i] + A[1][i])
print(dp[1][n - 1])
