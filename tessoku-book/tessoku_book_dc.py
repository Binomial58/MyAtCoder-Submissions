import math
def factorial(a):
    s=1
    while a!=1 and a!=0:
        s*=a
        s%=1000000007
        a-=1
    return s
def fermat(a):
    B=[a]
    for i in range(math.ceil(math.log2(1000000005))):
        B.append(B[-1]**2%1000000007)
    A=[]
    c=1000000005
    while c!=1 and c!=0:
        A.append(c%2)
        c//=2
    A.append(c)
    y=1
    for i in range(len(A)):
        if A[i]==1:
            y*=B[i]
            y%=1000000007
    return y
a,b=map(int, input().split())
n=a+b-2
r=a-1
x=factorial(n)
C=[x,fermat((factorial(r)*factorial(n-r))%1000000007)]
s=1
for c in C:
    s*=c
    s%=1000000007
print(s)
