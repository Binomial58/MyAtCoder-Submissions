n = int(input())
A = list(map(int, input().split()))
dp = [[0 for i in range(10)] for i in range(n)]
dp[0][A[0]] = 1
mod = 998244353
for i in range(1, n):
    for j in range(10):
        dp[i][(A[i] + j) % 10] += dp[i - 1][j]
        dp[i][(A[i] * j) % 10] += dp[i - 1][j]
    for j in range(10):
        dp[i][(A[i] + j) % 10] %= mod
        dp[i][(A[i] * j) % 10] %= mod
for i in range(10):
    print(dp[-1][i] % mod)
