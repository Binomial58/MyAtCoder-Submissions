N=int(input())
X=[[0]*100 for _ in range(100)]
S=0
for a in range(N):
    A,B,C,D=map(int, input().split())
    for i in range(A,B):
        for j in range(C,D):
            X[i][j]=1
for k in range(100):
    S+=sum(X[k])
print(S) 