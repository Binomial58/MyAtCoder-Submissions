N,Q=map(int, input().split())
A=list(map(int, input().split()))
S=set()
D=0
for i in range(Q):
    if A[i] not in S:
        if (A[i]+1) in S and (A[i]-1) in S:
            D-=1
            print(D)
        elif (A[i]+1) in S or (A[i]-1) in S:
            print(D)
        else:
            D+=1
            print(D)
        S.add(A[i])
    else:
        if (A[i]+1) in S and (A[i]-1) in S:
            D+=1
            print(D)
        elif (A[i]+1) in S or (A[i]-1) in S:
            print(D)
        else:
            D-=1
            print(D)
        S.remove(A[i])
