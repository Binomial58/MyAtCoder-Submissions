n=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
dp=[0 for i in range(n)]
dp[0]=0
dp[1]=A[0]
for i in range(n-2):
    dp[i+2]=min(dp[i+1]+A[i+1],dp[i]+B[i])
i=n-1
R=[n]
while i!=0 and i!=1:
    if dp[i-2]+B[i-2]>=dp[i-1]+A[i-1]:
        R.append(i)
        i-=1
    else:
        R.append(i-1)
        i-=2
if i==1:
    R.append(1)
print(len(R))
print(*R[::-1])