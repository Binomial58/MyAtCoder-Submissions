n, c = map(int, input().split())
A = list(map(int, input().split()))
dp = [0 for i in range(n)]
if c > 0:
    dp[0] = max(0, A[0])
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + A[i], A[i])
    print(sum(A) - max(dp) + max(dp) * c)
    # print(dp)
else:
    dp[0] = min(0, A[0])
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + A[i], A[i])
    print(sum(A) - min(dp) + min(dp) * c)
