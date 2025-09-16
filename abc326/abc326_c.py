import bisect
n,m=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
now=0
for i in range(n):
    now=max(bisect.bisect_left(A,m+A[i])-i,now)
print(now)