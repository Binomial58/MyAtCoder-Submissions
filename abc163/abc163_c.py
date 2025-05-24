import collections
N=int(input())
A=list(map(int, input().split()))
B=collections.Counter(A)
for i in range(1,N+1):
    print(B[i])