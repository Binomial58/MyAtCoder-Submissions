n,a,b=map(int, input().split())
R=[None for i in range(n+1)]
for i in range(a):
    R[i]=0
for j in range(a,b+1):
    R[j]=1
for k in range(b+1,n+1):
    if R[k-a]+R[k-b]==0 or R[k-a]+R[k-b]==1:
        R[k]=1
    else:
        R[k]=0
if R[n]==1:
    print("First")
else:
    print("Second")