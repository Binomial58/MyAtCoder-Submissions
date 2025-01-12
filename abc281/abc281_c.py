N,T=map(int, input().split())
A=list(map(int, input().split()))
S=sum(A)
D=T%S
for i in range(N):
    if D>=A[i]:
        D-=A[i]
    else:
        print(i+1,D)
        exit()