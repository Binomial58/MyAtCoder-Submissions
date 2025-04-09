N,H,W=map(int, input().split())
C=0
for _ in range(N):
    a,b=map(int, input().split())
    if a>=H and b>=W:
        C+=1
print(C)