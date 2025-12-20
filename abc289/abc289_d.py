n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
x = int(input())
dp = [[False for i in range(x + 1)] for j in range(n + 1)]
dp[0][0] = True
# print(dp)
for i in range(1, n + 1):
    for j in range(x + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
        if j in B:
            dp[i][j] = False
        if dp[i][j]:
            for k in A[:i]:
                if j + k < x + 1:
                    dp[i][j + k] = True
    # print(A[:i])
    # print(dp[i])
# print(dp)
if dp[n][x]:
    print("Yes")
else:
    print("No")
