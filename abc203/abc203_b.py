N,K=map(int, input().split())
S=0
for n in range(1,N+1):
    for k in range(1,K+1):
        S+=int(str(n)+str(0)+str(k))
print(S)