n=int(input())
A=list(map(int, input().split()))
dp=[[0 for i in range(n)]for i in range(n)]
for i in range(n):
    dp[n-1][i]=A[i]
if n%2==0:
    # 偶数の場合はmaxから始まる
    now=1
else:
    # 奇数の場合はminから始まる
    now=0
for i in range(n-1,0,-1):
    if now==0:
        for j in range(i):
            dp[i-1][j]=min(dp[i][j],dp[i][j+1])
            now=1
    else:
        for j in range(i):
            dp[i-1][j]=max(dp[i][j],dp[i][j+1])
            now=0
print(dp[0][0])
