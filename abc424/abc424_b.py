n,m,k=map(int, input().split())
A=[[0 for i in range(m)]for j in range(n)]
R=[]
for i in range(k):
    a,b=map(int, input().split())
    A[a-1][b-1]+=1
    if sum(A[a-1])==m:
        R.append(a)
print(*R)
