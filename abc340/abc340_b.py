Q=int(input())
A=[]
R=[list(map(int, input().split())) for _ in range(Q)]
for k in range(Q):
    if R[k][0]==1:
        A.append(R[k][1])
    else:
        print(A[len(A)-R[k][1]])