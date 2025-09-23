n=int(input())
P=[]
A=[]
l=0
r=n-1
for i in range(n):
    p,a=map(int, input().split())
    P.append(p-1)
    A.append(a)
dp=[[0 for i in range(n)] for j in range(n)]
width=r-l
for i in range(width-1,-1,-1):
    for j in range(n-i):
        # l=j
        # r=j+i
        if j==0:
            if j<=P[j+i+1]<=j+i:
                dp[j][j+i]=dp[j][j+i+1]+A[j+i+1]
            else:
                dp[j][j+i]=dp[j][j+i+1]
        elif j+i==n-1:
            if j<=P[j-1]<=j+i:
                dp[j][j+i]=dp[j-1][j+i]+A[j-1]
            else:
                dp[j][j+i]=dp[j-1][j+i]
        else:
            a=0
            b=0
            if j<=P[j+i+1]<=j+i:
                a=dp[j][j+i+1]+A[j+i+1]
            if j<=P[j-1]<=j+i:
                b=dp[j-1][j+i]+A[j-1]
            dp[j][j+i]=max(a,b,dp[j][j+i+1],dp[j-1][j+i])
        # print(j,j+i)
r=0
for i in range(n):
    r=max(r,dp[i][i])
print(r)