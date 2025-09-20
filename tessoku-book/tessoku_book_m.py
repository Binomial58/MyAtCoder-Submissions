n,k=map(int, input().split())
A=list(map(int, input().split()))
R=[0 for i in range(n)]
i=0
r=0
j=1
while i!=n and j<n:
    if A[j]<=k+A[i]:
        r+=1
        j+=1
    else:
        R[i]=r
        i+=1
    if j == n:
        for a in range(i,n):
            R[a]=r
        i=n
count=0
for i in range(n):
    count+=R[i]-i
print(count)