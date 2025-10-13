n,m=map(int, input().split())
E=[[] for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    E[a-1].append(b)
    E[b-1].append(a)
for i in range(n):
    string=""
    string+=str(i+1)
    string+=":"
    string+=" {"
    p=", ".join(str(n) for n in E[i])
    string+=p
    string+="}"
    print(string)
