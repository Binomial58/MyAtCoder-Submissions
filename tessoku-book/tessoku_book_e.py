n,k=map(int, input().split())
count=0
for r in range(1,n+1):
    for b in range(1,n+1):
        if 1<=k-r-b<=n:
            count+=1
print(count)