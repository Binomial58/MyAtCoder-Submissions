n,q=map(int, input().split())
A=[0 for i in range(n)]
for i in range(q):
    l,r,t=map(int, input().split())
    for j in range(l-1,r):
        A[j]=t
for a in A:
    print(a)