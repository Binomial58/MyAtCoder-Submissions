N,L,R=map(int, input().split())
A=list(map(int, input().split()))
B=[]
for i in range(N):
    if A[i]>=R:
        B.append(R)
    elif A[i]<=L:
        B.append(L)
    else:
        B.append(A[i])
print(*B)