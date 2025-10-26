import collections
n=int(input())
A=list(map(int, input().split()))
C=collections.Counter(A)
count=0  
for c in C:
    k=C[c]
    count+=(k*(k-1)//2)*(n-k)
print(count)