n = int(input())
W, H, B = [], [], []
s = 0
for i in range(n):
    w, h, b = map(int, input().split())
    s += w
    W.append(w)
    H.append(h)
    B.append(b)
dp = [[-(10**9) for i in range(s // 2 + 1)] for i in range(n + 1)]
dp[0][0] = 0
for j in range(1, n + 1):
    for i in range(s // 2 + 1):
        if dp[j - 1][i] >= 0:
            dp[j][i] = max(dp[j][i], dp[j - 1][i] + B[j - 1])
        if i - W[j - 1] >= 0:
            dp[j][i] = max(dp[j][i], dp[j - 1][i - W[j - 1]] + H[j - 1])
print(max(dp[n]))
