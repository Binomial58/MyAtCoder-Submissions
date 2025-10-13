def bin(N):
    C = ""
    while N != 0:
        C += str(N % 2)
        N //= 2
    D = ""
    for i in range(len(C)):
        D += C[len(C) - i - 1]
    return D

n,q=map(int, input().split())
A=list(map(int, input().split()))
dp=[[0 for i in range(n)]for i in range(31)]
R=[]
for i in range(n):
    dp[0][i]=A[i]
for i in range(1,31):
    for j in range(n):
        dp[i][j]=dp[i-1][dp[i-1][j]-1]
for i in range(q):
    x,y=map(int, input().split())
    now=x-1
    j=0
    t=bin(y)[::-1]
    for s in t:
        if s=="1":
            now=dp[j][now]-1
        j+=1
    R.append(now+1)
for r in R:
    print(r)