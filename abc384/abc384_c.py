#部分集合を列挙するためのライブラリ
import itertools
a,b,c,d,e=map(int, input().split())
date=["A","B","C","D","E"]
T=[]
K=[]
#リスト内の要素の全ての組み合わせの出力
for k in range(1,6):
    for subset in itertools.combinations(date,k):
        T.append("".join(subset))
for i in range(31):
    S=0
    if T[i].count("A")==1:
        S+=a
    if T[i].count("B")==1:
        S+=b
    if T[i].count("C")==1:
        S+=c
    if T[i].count("D")==1:
        S+=d
    if T[i].count("E")==1:
        S+=e
    K.append(S)
U=[[T[i],K[i]] for i in range(31)]
#降順でソートして同じ値の場合辞書式でソートする
result=sorted(U,key=lambda x:(-x[1],x[0]))
for j in range(31):
    print(result[j][0])