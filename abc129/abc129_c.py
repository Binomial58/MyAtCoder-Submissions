n, m = map(int, input().split())
dp = [0 for i in range(n + 1)]
A = set()
for i in range(m):
    A.add(int(input()))
dp[0] = 1
if 1 not in A:
    dp[1] = 1
for i in range(2, n + 1):
    if i not in A:
        dp[i] = dp[i - 1] + dp[i - 2]
        dp[i] %= 1000000007
print(dp[-1])
