N,X=map(int, input().split())
L=list(map(int, input().split()))
S=0
C=1
for i in range(N):
    S+=L[i]
    if S<=X:
        C+=1
print(C)