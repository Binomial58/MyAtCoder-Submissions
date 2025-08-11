n,a,b=map(int, input().split())
d=abs(a-b)
if d%2==0:
    print(d//2)
else:
    c=min(min(a,b)-1,n-max(a,b))
    print(c+d//2+1)