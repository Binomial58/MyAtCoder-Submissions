import collections
N=int(input())
A=list(map(int, input().split()))
B=collections.Counter(A)
M=0
for a in A:
    if B[a]==1:
        M=max(M,a)
if M==0:
    print(-1)
else:
    print(A.index(M)+1)