import bisect
n=int(input())
A=list(map(int, input().split()))
B=[]
dp=[-10**9]*n
dp[0]=1
B.append(A[0])
for i in range(1,n):
    j=bisect.bisect_left(B,A[i])
    if len(B)==j:
        B.append(A[i])
    else:
        B[j]=min(B[j],A[i])
    dp[i]=j+1
print(max(dp))