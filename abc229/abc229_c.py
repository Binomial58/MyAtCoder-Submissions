N,W=map(int, input().split())
X=[]
Y=[]
D=0
for i in range(N):
    x,y=map(int, input().split())
    X.append(x)
    Y.append(y)
X,Y=zip(*sorted(zip(X, Y) ,reverse=True))
for i in range(N):
    if W>=Y[i]:
        D+=X[i]*Y[i]
        W-=Y[i]
    else:
        D+=X[i]*W
        W-=W
print(D)