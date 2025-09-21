n=int(input())
H=list(map(int, input().split()))
dp=[0 for i in range(n)]
dp[0]=0
dp[1]=abs(H[0]-H[1])
for i in range(n-2):
    dp[i+2]=min(dp[i+1]+abs(H[i+2]-H[i+1]),dp[i]+abs(H[i+2]-H[i]))
print(dp[-1])