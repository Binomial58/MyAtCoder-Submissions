N,M=map(int, input().split())
par=[i for i in range(N+1)]
def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def same(x,y):
    return find(x)==find(y)
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return 0
    par[x]=y
for i in range(M):
    a,b=map(int, input().split())
    unite(a,b)
#連結成分の個数を数えている
root=set()
for i in range(1,N+1):
    root.add(find(i))
print(len(root)-1)