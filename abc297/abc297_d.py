a,b=map(int, input().split())
count=0
a,b=max(a,b),min(a,b)
while a!=b and b!=0:
    q=a//b
    r=a%b
    count+=q
    a=b
    b=r
if count!=0:
    print(count-1)
else:
    print(count)