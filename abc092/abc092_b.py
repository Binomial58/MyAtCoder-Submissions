N=int(input())
D,X=map(int, input().split())
A=[int(input()) for _ in range(N)]
B=[1 for _ in range(N)]
for i in range(1,D+1):
    for j in range(N):
        if B[j] == i:
            X+=1
            B[j]+=A[j]
print(X)