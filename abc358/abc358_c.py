n,m=map(int, input().split())
shop=n
P=[]
for i in range(n):
    P.append(input())
for i in range(1<<n):
    S=[0 for i in range(m)]
    c=0
    for j in range(n):
        if (i>>j) & 1:
            c+=1
            for k in range(m):
                if P[j][k]=="o":
                    S[k]=1
    if S==[1 for i in range(m)]:
        shop=min(shop,c)
print(shop)