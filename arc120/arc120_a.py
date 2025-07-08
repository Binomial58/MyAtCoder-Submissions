import copy
N=int(input())
A=list(map(int, input().split()))
C=[A[0]]
for j in range(1,N):
    C.append(C[j-1]+A[j])
D=[0,C[0]]
for j in range(1,N):
    D.append(D[j]+C[j])
E=[A[0]]
for i in range(1,N):
    E.append(max(E[i-1],A[i]))
R=[]
for i in range(N):
    S=C[i]
    M=E[i]
    S+=M*(i+1)+D[i]
    R.append(S)
for r in R:
    print(r)
