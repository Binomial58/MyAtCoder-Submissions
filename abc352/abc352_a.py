N,X,Y,Z=map(int, input().split())
if (Y<Z and Z<X)or(X<Z and Z<Y):
    print("Yes")
else:
    print("No")