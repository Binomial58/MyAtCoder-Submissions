N=int(input())
A=[]
for i in range(N):
    C=list(map(int,input().split()))
    A.append(C)
F=A[0][0]
for k in range(2,N+1):
    d=k
    if d>F:
        F,d=d,F
    F=A[F-1][d-1]
print(F)