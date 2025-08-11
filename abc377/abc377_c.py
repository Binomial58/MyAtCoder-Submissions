n,m=map(int, input().split())
Cannot=set()
for i in range(m):
    a,b=map(int, input().split())
    S=[[a-2,b+1],[a-1,b+2],[a,b],[a+1,b+2],[a+2,b+1],[a+1,b-2],[a+2,b-1],[a-2,b-1],[a-1,b-2]]
    for s in S:
        if 1<=s[0]<=n and 1<=s[1]<=n:
            Cannot.add(str(s[0])+","+str(s[1]))
print(n**2-len(Cannot))