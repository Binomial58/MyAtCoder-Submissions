import math
N=int(input())
X=list(map(int, input().split()))
A=0
B=0
C=0
for x in X:
    A+=abs(x)
    B+=abs(x)**2
    C=max(C,abs(x))
B=math.sqrt(B)
print(A)
print(B)
print(C)