n=int(input())
h=list(map(int, input().split()))
dp=[0 for i in range(n)]
dp[0]=0
dp[1]=abs(h[0]-h[1])
R=[]
for i in range(n-2):
    dp[i+2]=min(dp[i]+abs(h[i+2]-h[i]),dp[i+1]+abs(h[i+2]-h[i+1]))
place=n
while True:
    R.append(place)
    if place==1:
        break
    if dp[place-1]==dp[place-2]+abs(h[place-2]-h[place-1]):
        place-=1
    else:
        place-=2
print(len(R))
print(*R[::-1])