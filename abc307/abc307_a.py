N=int(input())
A=list(map(int, input().split()))
D=[]
for i in range(N):
    D.append(sum(A[i*7:(i+1)*7]))
print(*D)