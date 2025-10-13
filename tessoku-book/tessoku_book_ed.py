def Cal(n):
    if n!=0:
        s=n
        n=str(n)
        for i in n:
            s-=int(i)
        return s
    else:
        return 0
    
def bin(N):
    C = ""
    while N != 0:
        C += str(N % 2)
        N //= 2
    D = ""
    for i in range(len(C)):
        D += C[len(C) - i - 1]
    return D

n,k=map(int, input().split())
dp=[[0 for i in range(n+1)] for i in range(31)]
R=[]
for i in range(n+1):
    dp[0][i]=Cal(i)
for i in range(1,31):
    for j in range(n+1):
        dp[i][j]=dp[i-1][dp[i-1][j]]
for i in range(1,n+1):
    now=i
    j=0
    t=bin(k)[::-1]
    for s in t:
        if s=="1":
            now=dp[j][now]
        j+=1
    R.append(now)
for r in R:
    print(r)