N,M,X=map(int, input().split())
A=list(map(int, input().split()))
B=[0]*N
for a in A:
    B[a-1]=1
print(min(sum(B[:X-1]),sum(B[X:])))