N,M=map(int, input().split())
D={i for i in range(1,M+1)}
for i in range(N):
    K=list(map(int, input().split()))
    A=set(K[1:])
    D&=A
print(len(D))