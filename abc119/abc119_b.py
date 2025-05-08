N=int(input())
S=0
for _ in range(N):
    x,u=map(str, input().split())
    if u=="JPY":
        S+=int(x)
    else:
        S+=380000.0*float(x)
print(S)