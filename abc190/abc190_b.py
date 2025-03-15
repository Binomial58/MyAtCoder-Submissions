N,S,D=map(int, input().split())
X=[]
Y=[]
c=0
for _ in range(N):
    x,y=map(int, input().split())
    X.append(x)
    Y.append(y)
for i in range(N):
    if X[i]<S and Y[i]>D:
        c+=1
    if c>0:
        print("Yes")
        exit()
print("No")
