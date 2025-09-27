n,m=map(int, input().split())
A=[list(map(int, input().split())) for i in range(m)]
dp=[[10**9 for i in range(2**n)]for i in range(m+1)]
dp[0][0]=0
for i in range(m):
    for j in range(2**n):
        s=""
        a=j
        while a!=1 and a!=0:
            s+=str(a%2)
            a//=2
        s+=str(a)
        s="0"*(n-len(s))+s[::-1]
        B=[int(s[b]) for b in range(n)][::-1]
        if dp[i][j]!=10**9:
            dp[i+1][j]=min(dp[i][j],dp[i+1][j])
            s=0
            for k in range(n):
                s+=int(A[i][k]|B[k])*(2**k)
            dp[i+1][s]=min(dp[i+1][s],dp[i][j]+1)
if dp[m][2**n-1]==10**9:
    print(-1)
else:
    print(dp[m][2**n-1])