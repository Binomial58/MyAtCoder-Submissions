n=int(input())
H=list(map(int, input().split()))
H=[0]+H+[0]
count=0
m=max(H)
now=True
for i in range(m):
    count+=1
    j=0
    while j!=n+2 and H[j]==0:
        j+=1
    k=n+1
    while k !=-1 and H[k]==0:
        k-=1
    for s in range(j,k+1):
        if  now and H[s]==0:
            count+=1
            now=not now
        elif not now and H[s]!=0:
            now=not now
    for j in range(n+2):
        H[j]=max(0,H[j]-1)
print(count)