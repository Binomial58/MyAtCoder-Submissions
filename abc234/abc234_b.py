import math
N=int(input())
X,Y=[],[]
L=[]
for _ in range(N):
    x,y=map(int, input().split())
    X.append(x)
    Y.append(y)
for a in range(N):
    for b in range(N):
        if a==b:
            break
        L.append(math.sqrt((X[a]-X[b])**2+(Y[a]-Y[b])**2))
print(max(L))