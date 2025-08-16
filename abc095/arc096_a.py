a,b,c,x,y=map(int, input().split())
c*=2
s=0
if a+b>c:
    s+=c*min(x,y)
    m=min(x,y)
    x-=m
    y-=m
    if x==0:
        if b>c:
            s+=y*c
        else:
            s+=y*b
    else:
        if a>c:
            s+=x*c
        else:
            s+=x*a
    print(s)
else:
    print(a*x+b*y)
