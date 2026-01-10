n, x = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
dp = [[False for i in range(x + 1)] for j in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(x + 1):
        if dp[i][j]:
            for k in range(A[i][1] + 1):
                if j + k * A[i][0] <= x:
                    dp[i + 1][j + k * A[i][0]] = True
                else:
                    break
                # print(k)
# print(A)
if dp[n][x]:
    print("Yes")
else:
    print("No")
