import math 
N=int(input())
m=100**10
for b in range(math.floor(math.log2(N)),-1,-1):
    a=N//(2**b)
    c=N-a*2**b
    m=min(m,a+b+c)
print(m)