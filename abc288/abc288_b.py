N,K=map(int, input().split())
T=[]
for _ in range(K):
    s=input()
    T.append(s)
for _ in range(N-K):
    s=input()
T.sort()
print(*T)