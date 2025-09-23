n,s=map(int, input().split())
A=list(map(int, input().split()))
dp=[[False for i in range(s+1)]for i in range(n+1)]
dp[0][0]=True
for j in range(1,n+1):
    for i in range(s+1):
        if dp[j-1][i]:
            dp[j][i]=True
        elif i-A[j-1]>=0 and dp[j-1][i-A[j-1]]:
            dp[j][i]=True
if dp[n][s]:
    print("Yes")
else:
    print("No")