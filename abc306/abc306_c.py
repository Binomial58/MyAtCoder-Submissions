import copy
N=int(input())
A=list(map(int, input().split()))
D=copy.deepcopy(A)
B=[i for i in range(3*N)]
A,B=zip(*sorted(zip(A,B)))
C=[B[1+3*k] for k in range(N)]
C.sort()
E=[D[k] for k in C]
print(*E)