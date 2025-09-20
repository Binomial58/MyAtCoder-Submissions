n,x=map(int, input().split())
A=list(map(int, input().split()))
l=0
r=n-1
i=(l+r)//2
while A[i]!=x:
    if A[i]<x:
        l=i+1
        i=(l+r)//2
    elif A[i]>x:
        r=i-1
        i=(l+r)//2
print(i+1)