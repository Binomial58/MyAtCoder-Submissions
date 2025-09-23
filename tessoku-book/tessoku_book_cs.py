s=input()
t=input()
# dp[len(t)][len(s)]
dp=[[0 for i in range(len(s)+1)] for i in range(len(t)+1)]
for i in range(len(s)+1):
    dp[0][i]=i
for j in range(len(t)+1):
    dp[j][0]=j
for i in range(1,len(t)+1):
    for j in range(1,len(s)+1):
        if s[j-1]==t[i-1]:
            dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1])
        else:
            dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
print(dp[len(t)][len(s)])