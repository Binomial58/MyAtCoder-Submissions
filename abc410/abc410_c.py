N,Q=map(int, input().split())
A=[i for i in range(1,N+1)]
C=[]
k=0
for q in range(Q):
    B=list(map(int, input().split()))
    if len(B)==2:
        a=B[0]
        b=B[1]
    else:
        a=B[0]
        b=B[1]
        c=B[2]
    if a==1:
        A[(b-1+k)%N]=c
    elif a==2:
        C.append(A[(b-1+k)%N])
    else:
        k+=b%N
for c in C:
    print(c)