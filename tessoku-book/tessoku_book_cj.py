import bisect
n=int(input())
A=list(map(int, input().split()))
A.sort()
q=int(input())
R=[]
for i in range(q):
    x=int(input())
    R.append(bisect.bisect_left(A,x))
for r in R:
    print(r)