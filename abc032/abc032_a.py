import math
a=int(input())
b=int(input())
n=int(input())
L=math.lcm(a,b)
D=L
while L<n:
    L+=D
print(L)