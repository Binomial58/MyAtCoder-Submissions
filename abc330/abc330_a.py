N,L=map(int, input().split())
A=list(map(int, input().split()))
S=0
for a in A:
    if a>=L:
        S+=1
print(S)