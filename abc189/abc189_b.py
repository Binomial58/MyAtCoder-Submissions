n,x=map(int, input().split())
V,P=[],[]
count=0
for i in range(n):
    v,p=map(int, input().split())
    V.append(v)
    P.append(p)
for i in range(n):
    k=V[i]*P[i]
    count+=k
    if count >x*100:
        print(i+1)
        exit()
print(-1)