import copy
N=int(input())
A=list(map(int, input().split()))
C=copy.deepcopy(A)
for i in range(N-1):
    M=len(A)
    B=[]
    for j in range(0,M,2):
        B.append(max(A[j],A[j+1]))
    A=copy.deepcopy(B)
print(C.index(min(A))+1)