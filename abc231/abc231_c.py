import bisect
N,Q=map(int, input().split())
A=list(map(int, input().split()))
A.sort()
X=[]
for i in range(Q):
    x=int(input())
    X.append(N-bisect.bisect(A,x-1))
for x in X:
    print(x)