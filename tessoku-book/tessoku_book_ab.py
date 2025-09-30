n=int(input())
now=0
for i in range(n):
    t,a=map(str, input().split())
    a=int(a)
    if t=="+":
        now+=a
    elif t=="-":
        now-=a
    else:
        now*=a
    now%=10000
    print(now)