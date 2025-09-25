n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
dp=[(10**9) for i in range(n)]
dp[0]=0
dp[1]=A[0]
for i in range(2,n):
    dp[i]=min(dp[i],dp[i-1]+A[i-1])
    dp[i]=min(dp[i],dp[i-2]+B[i-2])
print(dp[-1])