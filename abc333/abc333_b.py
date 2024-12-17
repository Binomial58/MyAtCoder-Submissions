S=input()
T=input()
R=["A","B","C","D","E"]
X=[R.index(S[0]),R.index(S[1])]
Y=[R.index(T[0]),R.index(T[1])]
DX=min(abs(X[0]-X[1]),5-abs(X[0]-X[1]))
DY=min(abs(Y[0]-Y[1]),5-abs(Y[0]-Y[1]))
if DX==DY:
    print("Yes")
else:
    print("No")