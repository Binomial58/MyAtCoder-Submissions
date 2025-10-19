s,a,b,x=map(int, input().split())
t=0
for i in range(1,x+1):
    if 0<i%(a+b)<=a:
        t+=s
print(t)
