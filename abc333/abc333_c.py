import itertools
A=[int("1"*i) for i in range(1,16)]
B=set()
n=int(input())
for v in itertools.combinations_with_replacement(A, 3):
    B.add(sum(v))
B=list(B)
B.sort()
print(B[n-1])