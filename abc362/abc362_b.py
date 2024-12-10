def distance2(a,b,c,d):
    return (a-c)**2+(b-d)**2

X_A,y_A=map(int, input().split())
X_B,y_B=map(int, input().split())
X_C,y_C=map(int, input().split())
X=distance2(X_A,y_A,X_B,y_B)
Y=distance2(X_B,y_B,X_C,y_C)
Z=distance2(X_C,y_C,X_A,y_A)
D=max(X,Y,Z)
if X+Y+Z-D==D:
        print("Yes")
else:
        print("No")