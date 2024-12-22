import collections
N=int(input())
A=list(map(int, input().split()))
s=0
c=collections.Counter(A)
for i in set(A):
    s+=c[i]//2
print(s)