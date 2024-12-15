N=int(input())
A=[input()for _ in range(N)]
B=[input()for _ in range(N)]
for i in range(N):
    for k in range(N):
        if A[i][k]!=B[i][k]:
            print(i+1,k+1)
            exit()