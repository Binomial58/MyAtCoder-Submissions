import math
K=int(input())
S=0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            S+=math.gcd(a,b,c)
print(S)