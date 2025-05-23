N=int(input())
A=list(map(int, input().split()))
a=sum(A)/N
for i in range(N):
    A[i]=abs(A[i]-a)
print(A.index(min(A)))