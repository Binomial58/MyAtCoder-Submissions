N=int(input())
R=[0,0,0,0,0,0,0,0]
A=list(map(int, input().split()))
for i in range(N):
    for j in range(3,-1,-1):
        if R[j]==1:
            R[j]=0
            R[j+A[i]]+=1
    R[A[i]-1]=1
print(sum(R[3:]))