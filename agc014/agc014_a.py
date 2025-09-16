a,b,c=map(int, input().split())
count=0
if a%2==1 or b%2==1 or c%2==1:
    print(0)
    exit()
if a==b==c:
    print(-1)
else:
    while a%2!=1 and b%2!=1 and c%2!=1:
        ah=a//2
        bh=b//2
        ch=c//2
        count+=1
        a=bh+ch
        b=ah+ch
        c=bh+ah
    print(count)
