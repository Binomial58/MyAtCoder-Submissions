K=int(input())
X=list(map(int, input().split()))
B=set(i for i in range(1,K+1))
for x in range(K):
    #集合の中に指定した要素があるのか
    if x+1 in B:
        #集合から要素を削除
        B.discard(X[x])
print(len(B))
print(*(B))