n,a,b=map(int, input().split())
i=0
while n>0:
    if i==0:
        n-=a
        i=1
    else:
        n-=b
        i=0
if i==0:
    print("Bug")
else:
    print("Ant")