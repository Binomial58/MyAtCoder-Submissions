N=int(input())
A=list(map(int, input().split()))
d=0
for k in range(1,N+1):
    a,b=[i for i, x in enumerate(A) if x==k ]
    c=b-a
    if c==2:
        d+=1
print(d)