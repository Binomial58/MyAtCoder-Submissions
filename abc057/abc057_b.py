#マンハッタン距離を計算する関数
def manhattan(x,y,a,b) :
    return abs(x-a)+abs(y-b)
N,M=map(int, input().split())
X=[]
Y=[]
Z=[]
for i in range(N):
    x=list(map(int, input().split()))
    X.append(x)
for j in range(M):
    y=list(map(int, input().split()))
    Y.append(y)
for i in range(N):
    D=[]
    for j in range(M):
        D.append(manhattan(X[i][0],X[i][1],Y[j][0],Y[j][1]))
    Z.append(D.index(min(D))+1)
for z in Z:
    print(z)