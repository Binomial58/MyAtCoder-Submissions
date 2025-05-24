N,S,T=map(int, input().split())
W=int(input())
C=0
if S<=W<=T:
    C+=1
for i in range(N-1):
    a=int(input())
    W+=a
    if S<=W<=T:
        C+=1
print(C)