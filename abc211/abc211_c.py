s = input()
dp = [[0 for i in range(8)] for j in range(len(s) + 1)]
T = ["c", "h", "o", "k", "u", "d", "a", "i"]
for i in range(1, len(s) + 1):
    for j in range(8):
        dp[i][j] = dp[i - 1][j] % (10**9 + 7)
    if s[i - 1] in T:
        # print(s[i - 1])
        if s[i - 1] == "c":
            dp[i][0] += 1
        else:
            ti = T.index(s[i - 1])
            dp[i][ti] += dp[i][ti - 1]
# for d in dp:
# print(d)
print(dp[-1][-1] % (10**9 + 7))
