x,y=map(int, input().split())
if x>=0:
    if y>0:
        if y>x:
            print(y-x)
        else:
            print(2+abs(x-y))
    elif y<0:
        if abs(y)>x:
            print(abs(y)-x+1)
        else:
            print(1+x+y)
    else:
        print(1+abs(x-y))
else:
    if y>0:
        if abs(x)<=y:
            print(1+x+y)
        else:
            print(1+abs(x+y))
    else:
        if x<y:
            print(abs(x-y))
        else:
            print(2+abs(x-y))