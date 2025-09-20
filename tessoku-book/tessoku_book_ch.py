n=int(input())
A=[[0 for i in range(1503)] for j in range(1503)]
for i in range(n):
    a,b,c,d=map(int, input().split())
    a+=1
    b+=1
    A[a][b]+=1
    A[a][d+1]-=1
    A[c+1][b]-=1
    A[c+1][d+1]+=1
B=[[0 for i in range(1503)] for j in range(1503)]
for i in range(1503):
    for j in range(1502):
        B[i][j+1]=B[i][j]+A[i][j+1]
for j in range(1503):
    for i in range(1502):
        B[i+1][j]+=B[i][j]
count=0
for i in range(len(B)):
    for j in range(len(B[i])):
        if B[i][j]>=1:
            count+=1
print(count)