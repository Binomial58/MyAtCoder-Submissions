a,b,x,y=map(int, input().split())
if a==b or a==b+1:
    print(x)
elif b>a:
    print(min(x+(b-a)*y,(1+2*(b-a))*x))
else:
    print(min(x+y*(a-b-1),x*(1+(a-b-1)*2)))