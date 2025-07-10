n,m=map(int, input().split())
left=1
right=n
for i in range(m):
    l,r=map(int, input().split())
    left=max(left,l)
    right=min(right,r)
print(max(right-left+1,0))