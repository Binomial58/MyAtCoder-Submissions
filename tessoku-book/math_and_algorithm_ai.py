n,q=map(int, input().split())
A=list(map(int, input().split()))
Asum=[0]
for i in range(n):
    Asum.append(Asum[i]+A[i])
R=[]
for i in range(q):
    l,r=map(int, input().split())
    R.append(Asum[r]-Asum[l-1])
for r in R:
    print(r)