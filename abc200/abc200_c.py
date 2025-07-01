import collections
N=int(input())
A=list(map(int, input().split()))
S=0
B=[a%200 for a in A]
C=collections.Counter(B)
B=list(set(B))
for b in B:
    S+=C[b]*(C[b]-1)//2
print(S)
