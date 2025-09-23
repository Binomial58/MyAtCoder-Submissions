n,w=map(int, input().split())
W=[]
V=[]
for i in range(n):
    a,b=map(int, input().split())
    W.append(a)
    V.append(b)
dp=[[-1 for i in range(w+1)]for i in range(n+1)]
dp[0][0]=0
for j in range(1,n+1):
    for i in range(w+1):
        if i-W[j-1]>=0:
            dp[j][i]=max(dp[j-1][i],dp[j-1][i-W[j-1]]+V[j-1])
        else:
            dp[j][i]=dp[j-1][i]
print(max(dp[n]))