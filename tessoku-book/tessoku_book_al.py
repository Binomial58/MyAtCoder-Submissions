d,n=map(int, input().split())
A=[24 for i in range(d)]
for i in range(n):
    l,r,h=map(int, input().split())
    for j in range(l-1,r):
        A[j]=min(A[j],h)
print(sum(A))