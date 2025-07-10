import bisect
n,m=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
B.sort()
t=10**10
for i in range(n):
    a=A[i]
    j=bisect.bisect(B,A[i])
    if j==0:
        t=min(t,abs(a-B[j]))
    elif j==m:
        t=min(t,abs(a-B[j-1]))
    else:
        t=min(t,abs(a-B[j]),abs(a-B[j-1]))
print(t)