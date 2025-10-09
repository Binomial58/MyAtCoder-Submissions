n,l=map(int, input().split())
maxe=0
maxw=0
for i in range(n):
    a,b=map(str, input().split())
    if b=="E":
        maxe=max(maxe,l-int(a))
    else:
        maxw=max(maxw,int(a))
print(max(maxw,maxe))