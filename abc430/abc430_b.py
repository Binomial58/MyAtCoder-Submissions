n,m=map(int, input().split())
s=[list(input()) for _ in range(n)]
B=set()
for i in range(n-m+1):
    for j in range(n-m+1):
        p=""
        for a in range(i,i+m):
            for b in range(j,j+m):
                p+=s[a][b]
        B.add(p)
print(len(B))