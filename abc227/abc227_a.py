N,K,A=map(int, input().split())
A-=1
for _ in range(K):
    if A==N:
        A=0
    A+=1
print(A)