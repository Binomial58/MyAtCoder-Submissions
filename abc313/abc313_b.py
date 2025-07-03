N,M=map(int, input().split())
R=[M for i in range(N)]
for i in range(M):
    a,b=map(int, input().split())
    R[b-1]-=1
if R.count(max(R))==1:
    print(R.index(max(R))+1)
else:
    print(-1)