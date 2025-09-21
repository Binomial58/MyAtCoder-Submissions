n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
dp=[0 for i in range(n)]
dp[1]=A[0]
for i in range(n-2):
    dp[i+2]=min(dp[i]+B[i],dp[i+1]+A[i+1])
print(dp[-1])
