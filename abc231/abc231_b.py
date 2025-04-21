import collections
N=int(input())
S=[]
for _ in range(N):
    s=input()
    S.append(s)
D=collections.Counter(S)
print(D.most_common()[0][0])
#出現回数をカウント