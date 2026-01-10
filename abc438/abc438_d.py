n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
As = [A[0]]
for i in range(1, n):
    As.append(As[i - 1] + A[i])
dp = [[0 for i in range(n)] for j in range(3)]
for i in range(n):
    dp[0][i] = As[i]
for i in range(1, n):
    if i > 1:
        dp[2][i] = max(dp[1][i - 1], dp[2][i - 1]) + C[i]
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1]) + B[i]
# for d in dp:
#     print(d)
print(dp[2][-1])
