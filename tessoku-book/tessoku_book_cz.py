a,b=map(int, input().split())
a,b=max(a,b),min(a,b)
c=a
d=b
r=-1
while r!=0:
    q=a//b
    r=a%b
    a=b
    b=r
print(c*d//a)