import collections
N=int(input())
A=list(map(int, input().split()))
B=collections.Counter(A)
C=list(set(A))
S=N*(N-1)//2
for i in C:
    n=B[i]
    S-=n*(n-1)//2
print(S)