t = int(input())
for i in range(t):
    n = int(input())
    R = list(map(int, input().split()))
    minr = min(R)
    mini = R.index(minr)
    # [最小値・最大値]
    dp = [-1 for i in range(n)]
    dp[mini] = minr
    # print("mini", mini)
    # print("左")
    count = 0
    for j in range(mini - 1, -1, -1):
        dp[j] = min(dp[j + 1] + 1, R[j])
    # print(dp)
    for j in range(1, mini):
        dp[j] = min(dp[j - 1] + 1, dp[j])
    # print(dp)
    for j in range(mini + 1, n):
        dp[j] = min(dp[j - 1] + 1, R[j])
    # print(dp)
    for j in range(n - 1, mini, -1):
        dp[j - 1] = min(dp[j - 1], dp[j] + 1)
    for j in range(n):
        count += R[j] - dp[j]
    # print(dp)
    # print(R)
    # print(dp)
    # print(R)
    print(count)
