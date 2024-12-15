import math
#ユークリッド距離関数の定義
def distance(x_1,y_1,x_2,y_2):
    return math.sqrt ((x_1-x_2)**2+(y_1-y_2)**2)

N=int(input())
C=[list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    T=[]
    for k in range(N):
        D=distance(C[i][0],C[i][1],C[k][0],C[k][1])
        T.append(D)
    print(T.index(max(T))+1)