h,w,n=map(int, input().split())
A=[[0 for i in range(w+2)]for j in range(h+2)]
for i in range(n):
    a,b,c,d=map(int, input().split())
    A[a][b]+=1
    A[a][d+1]-=1
    A[c+1][b]-=1
    A[c+1][d+1]+=1
B=[[0 for i in range(w+2)]for j in range(h+2)]
for i in range(h+1):
    for j in range(w):
        B[i][j+1]=B[i][j]+A[i][j+1]
for j in range(w+1):
    for i in range(h):
        B[i+1][j]+=B[i][j]
for i in range(h):
    print(*B[i+1][1:w+1])