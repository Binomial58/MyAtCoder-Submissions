N=int(input())
A=list(map(int, input().split()))
Q=[list(map(int, input().split())) for _ in range(N-1)]
for k in range(N-1):
    R=A[k]//Q[k][0]
    if R>0:
        A[k]-=Q[k][0]*R
        A[k+1]+=Q[k][1]*R
print(A[N-1])