N=int(input())
K=int(input())
X=int(input())
Y=int(input())
S=0
for i in range(1,N+1):
    if i<=K:
        S+=X
    else:
        S+=Y
print(S)