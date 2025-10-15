def manhattan(x, y, a, b):
    return abs(x - a) + abs(y - b)

n=int(input())
t0=0
x0=0
y0=0
r=True
for i in range(n):
    t,x,y=map(int, input().split())
    if t-t0<manhattan(x0,y0,x,y):
        r=False
    elif ((t-t0)-manhattan(x0,y0,x,y))%2!=0:
        r=False
    t0=t
    x0=x
    y0=y
if r:
    print("Yes")
else:
    print("No")