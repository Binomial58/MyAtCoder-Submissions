import math
a,b=map(int, input().split())
B=[a]
for i in range(math.ceil(math.log2(b))):
    B.append((B[-1]**2)%1000000007)
A=[]
while b!=1 and b!=0:
    A.append(b%2)
    b//=2
A.append(b)
now=1
for i in range(len(A)):
    if A[i]==1:
        now*=B[i]
print(now%1000000007)