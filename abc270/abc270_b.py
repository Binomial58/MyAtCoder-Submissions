X,Y,Z=map(int, input().split())
T=0
U=0
if 0<Y<X or 0>Y>X:
    T=10**10
else:
    T=abs(X)
if 0<Y<Z or 0>Y>Z:
    U=10**10
else:
    U=abs(Z)+abs(Z-X)
if U==T==10**10:
    print(-1)
else:
    print(min(U,T))