def turn(r):
    if r=="d":
        r="s"
        return r
    elif r=="s":
        r="a"
        return r
    elif r=="a":
        r="w"
        return r
    else:
        r="d"
        return r
def go(X,Y,r):
    if r=="d":
        X+=1
        return X,Y
    elif r=="s":
        Y-=1
        return X,Y
    elif r=="a":
        X-=1
        return X,Y
    else:
        Y+=1
        return X,Y
N=int(input())
T=input()
x,y=0,0
R="d"
for i in range(N):
    if T[i]=="S":
        x,y=go(x,y,R)
    else:
        R=turn(R)
print(x,y)