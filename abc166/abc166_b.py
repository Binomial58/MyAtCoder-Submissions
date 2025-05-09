N,K=map(int, input().split())
A=set([i for i in range(1,N+1)])
B=set([])
for i in range(K):
    d=int(input())
    C=set(list(map(int, input().split())))
    B=B|C
print(len(A-B))