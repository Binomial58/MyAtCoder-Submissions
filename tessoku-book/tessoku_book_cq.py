n,s=map(int, input().split())
A=list(map(int, input().split()))
dp=[[False for i in range(s+1)]for j in range(n+1)]
dp[0][0]=True
for i in range(1,n+1):
    for j in range(s+1):
        if dp[i-1][j]:
            dp[i][j]=True
        elif j-A[i-1]>=0 and dp[i-1][j-A[i-1]]:
            dp[i][j]=True
if dp[n][s]:
    used=[]
    for i in range(n):
        k=s
        if k-A[n-i-1]>=0 and dp[n-i][k-A[n-i-1]]:
            used.append(n-i)
            s-=A[n-i-1]
    print(len(used))
    print(*used[::-1])
else:
    print(-1)