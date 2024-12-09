N,C=map(int,input().split())
T=list(map(int,input().split()))
#飴の合計個数
S=1
#前回飴をもらった時の絶対時間
X=T[0]
for i in range(1,N):
    #前回飴をもらった時からの経過時間
    Y=T[i]-X
    if Y>=C:
        S+=1
        X=T[i]
print(S)