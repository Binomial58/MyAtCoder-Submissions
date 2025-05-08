import math
N=int(input())
k=math.floor(math.log2(N))
if 2**k<=N:
    print(math.floor(math.log2(N)))
else:
    print(math.floor(math.log2(N))-1)