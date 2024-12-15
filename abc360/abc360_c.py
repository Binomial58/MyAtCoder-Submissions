from collections import defaultdict

N=int(input())
A=list(map(int, input().split()))
W=list(map(int, input().split()))

#defaultdictクラスを使用して空のリストを返す辞書の作成
D=defaultdict(list)
#Dのaという場所にwをリストの要素として追加
for a,w in zip(A,W):
    D[a].append(w)
S=sum(W)

for k in D:
    S-=max(D[k])
print(S)