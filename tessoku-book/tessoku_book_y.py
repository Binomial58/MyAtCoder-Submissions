h,w=map(int, input().split())
C = [list(input()) for _ in range(h)]
dp=[[-1 for i in range(w)] for i in range(h)]
for i in range(w):
    if C[0][i]==".":
        dp[0][i]=1
    else:
        break
for i in range(h):
    if C[i][0]==".":
        dp[i][0]=1
    else:
        break
for i in range(1,h):
    for j in range(1,w):
        if C[i][j]!="#":
            if dp[i-1][j]==-1:
                dp[i][j]=max(dp[i][j],dp[i][j-1])
            if dp[i][j-1]==-1:
                dp[i][j]=max(dp[i][j],dp[i-1][j])
            if dp[i][j-1]!=-1 and dp[i-1][j]!=-1:
                dp[i][j]=max(dp[i][j],dp[i-1][j]+dp[i][j-1])
if dp[h-1][w-1]==-1:
    print(0)
else:
    print(dp[h-1][w-1])