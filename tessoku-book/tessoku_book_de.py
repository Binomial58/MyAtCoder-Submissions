n,k=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
minA=A[0]
maxA=A[-1]
dp=[False for i in range(n+1)]
for i in range(1,n+1):
    for a in A:
        if i-a>=0:
            if not dp[i-a]:
                dp[i]=True
                continue
if dp[n]:
    print("First")
else:
    print("Second")