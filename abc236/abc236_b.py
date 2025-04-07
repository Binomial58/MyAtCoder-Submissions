N=int(input())
A=list(map(int, input().split()))
B=[4]*N
for i in range(4*N-1):
    B[A[i]-1]-=1
print(B.index(1)+1)