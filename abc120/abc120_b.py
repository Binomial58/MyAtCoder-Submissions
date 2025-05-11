A,B,K=map(int, input().split())
C=0
i=min(A,B)+1
while C!=K:
    i-=1
    if A%i==0 and B%i==0:
        C+=1
print(i)