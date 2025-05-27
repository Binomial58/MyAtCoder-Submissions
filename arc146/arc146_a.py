import itertools
N=int(input())
A=list(map(int, input().split()))
A.sort(reverse=True)
B=A[:3]
R=[0,1,2]
M=0
D=list(itertools.permutations(R))
for d in D:
    m=int(str(B[d[0]])+str(B[d[1]])+str(B[d[2]]))
    M=max(m,M)
print(M)