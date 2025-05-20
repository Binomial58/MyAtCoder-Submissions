A,B,M=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
m=min(a)+min(b)
for i in range(M):
    x,y,c=map(int, input().split())
    m=min(a[x-1]+b[y-1]-c,m)
print(m)