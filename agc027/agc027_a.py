N,x=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
if x<=sum(a):
    c=0
    i=0
    while c<x and x-c>=a[i]:
        c+=a[i]
        i+=1
    print(i)
else:
    a.sort(reverse=True)
    x-=sum(a)
    c=x
    i=N
    while c>0:
        c-=a[N-i]
        i-=1
    print(i)