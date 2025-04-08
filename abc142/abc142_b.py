N,K=map(int, input().split())
H=map(int, input().split())
C=0
for h in H:
    if h >=K:
        C+=1
print(C)