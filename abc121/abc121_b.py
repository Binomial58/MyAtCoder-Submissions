N,M,C=map(int, input().split())
B=list(map(int, input().split()))
T=0
for _ in range(N):
    a=list(map(int, input().split()))
    S=C
    for i in range(M):
        S+=a[i]*B[i]
    if S>0:
        T+=1
print(T)