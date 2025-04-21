N=int(input())
P=list(map(int, input().split()))
L=[0]*N
for i in range(N):
    L[P[i]-1]=i+1
print(*L)