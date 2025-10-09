n,m=map(int, input().split())
A=list(map(int, input().split()))
B=[m for i in range(n)]
for a in A:
    B[a-1]-=1
for b in B:
    print(b)