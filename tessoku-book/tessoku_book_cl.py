n,k=map(int, input().split())
A=list(map(int, input().split()))
sumA=[0]
R=[0 for i in range(n)]
for i in range(n):
    sumA.append(sumA[i]+A[i])
j=1
i=0
r=0
while i!=n+1 and j<n+1:
    if sumA[j]-sumA[i]<=k:
        r+=1
        j+=1
    else:
        R[i]=r
        i+=1
    if j==n+1:
        for a in range(i,n):
            R[a]=r
        i=n
count=0
for i in range(n):
    count+=R[i]-i
print(count)