import copy
N=int(input())
A=[]
for i in range(N):
    a=int(input())
    A.append(a)
B=copy.deepcopy(A)
B.sort(reverse=True)
M=B[0]
m=B[1]
for a in A:
    if a ==M:
        print(m)
    else:
        print(M)