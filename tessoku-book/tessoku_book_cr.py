n,w=map(int, input().split())
W=[]
V=[]
for i in range(n):
    a,b=map(int, input().split())
    W.append(a)
    V.append(b)
s=sum(V)
dp=[[-1 for i in range(s+1)] for j in range(n+1)]
dp[0][0]=w
for i in range(1,n+1):
    for j in range(s+1):
        if j-V[i-1]>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-V[i-1]]-W[i-1])
        else:
            dp[i][j]=dp[i-1][j]
for i in range(s,-1,-1):
    if dp[n][i]>=0:
        print(i)
        exit()